import rdflib
import json

from pathlib import Path
from typing import Union, Optional, List

from dacite import from_dict

from cell_annotation_schema.datamodel.cell_annotation_schema import Taxonomy
from cell_annotation_schema.datamodel.bican.cell_annotation_schema import BicanTaxonomy
from cell_annotation_schema.datamodel.cap.cell_annotation_schema import CapTaxonomy

from cell_annotation_schema.ontology.schema import CAS_ROOT_CLASS, DEFAULT_PREFIXES, CAS_NAMESPACE
from cell_annotation_schema.file_utils import get_json_from_file, get_cas_schema_names

from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime import SchemaView
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import rdflib_dumper
from linkml.validator import Validator
from linkml import generators

CELL_RELATION = "has_cellid"


def dump_to_rdf(
        schema: Union[str, Path, dict],
        instance: Union[str, dict],
        ontology_namespace: str,
        ontology_iri: str,
        schema_name: str = None,
        labelsets: Optional[List[str]] = None,
        output_path: str = None,
        validate: bool = True,
        include_cells: bool = True,
) -> rdflib.Graph:
    """
    Dumps the given data to an RDF file based on the provided schema.
    Args:
        schema (Union[str, Path, dict]): The schema path, dictionary, or file to be used for RDF generation.
        instance (Union[str, dict]): The data JSON file path or JSON object dictionary.
        ontology_namespace (str): Namespace of the ontology (e.g., `MTG`).
        ontology_iri (str): IRI of the ontology (e.g., `https://purl.brain-bican.org/ontology/AIT_MTG/`).
        schema_name (str): The name of the schema to be used for RDF generation (one of 'base', 'bican', 'cap' or None for other schemas).
        labelsets (Optional[List[str]]): Labelsets used in the taxonomy, such as `["Cluster", "Subclass", "Class"]`.
        output_path (Optional[str]):  Path to the output RDF file, if specified.
        validate (bool): Determines if data-schema validation checks will be performed. True by default.
        include_cells (bool): Determines if cell data will be included in the RDF output. True by default.
    Returns:
        An RDFlib graph object.
    """
    schema_def: SchemaDefinition = yaml_loader.load(
        schema, target_class=SchemaDefinition
    )

    if isinstance(instance, str):
        instance = get_json_from_file(instance)
    instance = remove_empty_strings(instance)

    if validate:
        validate_data(schema_def, instance)
    instance = serialise_author_annotation(instance)

    root_class = get_root_class(schema_name)
    py_inst = get_py_instance(instance, None, schema_def, root_class)

    prefixes = DEFAULT_PREFIXES.copy()
    prefixes["_base"] = ontology_iri
    prefixes[ontology_namespace] = ontology_iri
    for labelset in labelsets:
        prefixes[labelset] = ontology_iri + f"{labelset}#"

    g = rdflib_dumper.as_rdf_graph(
        py_inst,
        schemaview=SchemaView(schema_def),
        prefix_map=prefixes,
    )

    add_cl_existential_restrictions(g)
    if not include_cells:
        g.remove((None, rdflib.URIRef(CAS_NAMESPACE + "/" + CELL_RELATION), None))

    if output_path:
        g.serialize(format="xml", destination=output_path)
    return g


def get_py_instance(instance_dict, schema_name, schema_def, root_class=None):
    """
    Returns a Python instance of the schema class from the given data instance.
    Args:
        instance_dict: The data instance dictionary.
        schema_name: The name of the schema to be used for RDF generation.
        schema_def: The schema definition object.
        root_class: The root class of the schema if this is not a core (base,cap or bican) schema.
    Returns:
        The Python instance of the schema class.
    """
    if isinstance(schema_name, str):
        if schema_name.lower() == "base":
            return Taxonomy(**instance_dict)
        elif schema_name.lower() == "bican":
            return BicanTaxonomy(**instance_dict)
        elif schema_name.lower() == "cap":
            return CapTaxonomy(**instance_dict)

    # unknown schema, dynamically generate the python module and instantiate
    gen = generators.PythonGenerator(schema_def)
    output = gen.serialize()
    python_module = compile_python(output)
    py_target_class = getattr(python_module, root_class)
    py_inst = py_target_class(**instance_dict)

    return py_inst


def get_root_class(schema_name):
    """
    Returns the root class of the schema based on the schema name.
    Args:
        schema_name: The name of the schema.
    Returns: The root class of the schema.
    """
    root_class = None
    if schema_name.lower() == "base":
        root_class = CAS_ROOT_CLASS
    elif schema_name.lower() == "bican":
        root_class = "BicanTaxonomy"
    elif schema_name.lower() == "cap":
        root_class = "CapTaxonomy"
    return root_class


def add_cl_existential_restrictions(g: rdflib.Graph):
    """
    Adds existential restrictions to the CL class in the given RDF graph.
    Args:
        g: The RDF graph to be updated.
    """
    sparql_query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
        PREFIX RO: <http://purl.obolibrary.org/obo/RO_>


        DELETE {
            ?annotation RO:0002473 ?cl_term .
        }
        INSERT { 
            ?annotation rdf:type [
                a  owl:Restriction ;
               owl:onProperty  RO:0002473 ;
               owl:someValuesFrom ?cl_term
            ] .
        }
        WHERE {
          ?annotation a PCL:0010001.
          ?annotation RO:0002473 ?cl_term .
        }
    """
    g.update(sparql_query)


def validate_data(schema: SchemaDefinition, instance: dict) -> bool:
    """
    Validates the given data instance against the specified schema.
    Args:
        schema (SchemaDefinition): The schema to be used for the validation.
        instance (dict): The data instance to be validated.
    Returns:
        bool: Returns `True` if the data is valid; otherwise, logs the validation errors and raises an exception.
    """

    validator = Validator(schema)
    report = validator.validate(instance)
    if report.results:
        print("Validation errors ({}):".format(len(report.results)))
        for result in report.results:
            print(result)
        raise ValueError(
            "Data file is not valid against the schema. {} validation errors found.".format(
                len(report.results)
            )
        )

    print("Data file is valid against the schema.")
    return True


def populate_ids(
        instance: Union[str, Path, dict], ontology_namespace: str, ontology_id: str
) -> dict:
    """
    Populates ID fields in the data instance required for RDF conversion. Updates the instance in-place if it is a
    dictionary.
    Args:
        instance (Union[str, Path, dict]): The data JSON file path or JSON object dictionary.
        ontology_namespace (str): The namespace of the ontology, such as 'MTG'.
        ontology_id (str): The ontology ID to be used for the instance, such as 'AIT_MTG'.
    Returns:
        dict: A JSON object with populated ID properties.
    """

    if isinstance(instance, Path):
        instance = str(instance)
    if isinstance(instance, str):
        data = get_json_from_file(instance)
        if data is None:
            raise ValueError("No such file: " + instance)
        instance = data

    if "id" in instance and instance["id"]:
        return instance

    if "id" not in instance:
        if "CAS:" not in ontology_id:
            ontology_id = "CAS:" + ontology_id
        instance["id"] = ontology_id

    for labelset in instance.get("labelsets", []):
        if "id" not in labelset:
            labelset["id"] = f"{ontology_namespace}:{labelset['name']}"

    # TODO add id to other properties as well

    return instance


def remove_empty_strings(json_data: dict) -> Union[dict, list]:
    """
    Recursively removes empty strings from the given JSON data.
    Args:
        json_data (dict): The JSON data to be cleaned.
    Returns:
        dict: JSON data with all empty strings removed.
    """
    if isinstance(json_data, dict):
        return {
            key: remove_empty_strings(value)
            for key, value in json_data.items()
            if value != ""
        }
    elif isinstance(json_data, list):
        return [remove_empty_strings(item) for item in json_data if item != ""]
    else:
        return json_data


def serialise_author_annotation(instance: dict) -> dict:
    """
    Author annotations field value is a dict and needs to be serialised to a json string for better representation in RDF.
    Serialises the author annotation data in the instance to a json string.
    Args:
        instance: The instance to be updated.
    Returns:
        The updated instance.
    """
    for annotation in instance.get("annotations", []):
        if "author_annotation_fields" in annotation and annotation["author_annotation_fields"]:
            annotation["author_annotation_fields"] = json.dumps(annotation["author_annotation_fields"])
    return instance
