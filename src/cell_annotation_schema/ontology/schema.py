import requests

from typing import Union, Optional, List
from ruamel.yaml import YAML

from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.utils.schema_as_dict import schema_as_dict
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import json_dumper

from schema_automator.utils.schemautils import write_schema
from schema_automator.importers.jsonschema_import_engine import JsonSchemaImportEngine

from oaklib.utilities.subsets.value_set_expander import (
    ValueSetExpander,
    ValueSetConfiguration,
)


CAS_ROOT_CLASS = "Taxonomy"

CAS_NAMESPACE = "https://cellular-semantics.sanger.ac.uk/ontology/CAS"
CAS_ROOT_NS = "cell_annotation_schema"
DEFAULT_PREFIXES = {
    CAS_ROOT_NS: CAS_NAMESPACE + "/",
    "CAS": CAS_NAMESPACE + "/",
    "obo": "http://purl.obolibrary.org/obo/",
    "CL": "http://purl.obolibrary.org/obo/CL_",
    "PCL": "http://purl.obolibrary.org/obo/PCL_",
    "RO": "http://purl.obolibrary.org/obo/RO_",
    "skos": "http://www.w3.org/2004/02/skos/core#",
}


def decorate_linkml_schema(
    schema_obj: Union[dict, SchemaDefinition],
    ontology_namespace: str,
    ontology_iri: str,
    labelsets: Optional[List[str]] = None,
    output_path: Optional[str] = None,
) -> dict:
    """
    Adds additional properties to the LinkML schema necessary for OWL conversion.
    Args:
        schema_obj (Union[dict, SchemaDefinition]): The LinkML schema object, either as a dictionary or a
        SchemaDefinition.
        ontology_namespace (str): The namespace of the ontology (e.g., 'MTG').
        ontology_iri (str): The ontology IRI (e.g., 'https://purl.brain-bican.org/ontology/AIT_MTG/').
        labelsets (Optional[List[str]]): Labelsets used in the taxonomy, such as ['Cluster', 'Subclass', 'Class'].
        output_path (Optional[str]): Path to the output schema file, if specified.
    Returns:
        dict: The schema decorated with additional properties for OWL conversion.
    """

    if isinstance(schema_obj, SchemaDefinition):
        schema_obj = schema_as_dict(schema_obj)

    # schema_obj["id"] = CAS_NAMESPACE

    ontology_namespace = ontology_namespace.upper()
    # prefixes = DEFAULT_PREFIXES.copy()
    # prefixes["linkml"] = "https://w3id.org/linkml/"
    prefixes = schema_obj["prefixes"]
    prefixes["_base"] = ontology_iri
    prefixes[ontology_namespace] = ontology_iri
    labelsets = labelsets or []
    for labelset in labelsets:
        prefixes[labelset] = ontology_iri + f"{labelset}#"

    schema_obj["prefixes"] = prefixes
    # schema_obj["default_range"] = "string"
    # schema_obj["default_curi_maps"] = ["semweb_context", "obo_context"]
    # schema_obj["enums"]["CellTypeEnum"] = {
    #     "reachable_from": {
    #         "source_ontology": "obo:cl",
    #         "source_nodes": ["CL:0000000"],
    #         "include_self": True,
    #         "relationship_types": ["rdfs:subClassOf"],
    #     }
    # }
    schema_obj["slots"]["id"] = {"identifier": True, "range": "uriorcurie"}
    # schema_obj["slots"]["name"]["slot_uri"] = "rdfs:label"
    # schema_obj["slots"]["description"]["slot_uri"] = "IAO:0000115"
    # schema_obj["slots"]["cell_label"]["slot_uri"] = "rdfs:label"
    # schema_obj["slots"]["cell_fullname"]["slot_uri"] = "skos:preflabel"
    # schema_obj["slots"]["cell_ontology_term_id"]["slot_uri"] = "RO:0002473"
    # schema_obj["slots"]["cell_ontology_term_id"]["range"] = "CellTypeEnum"
    # schema_obj["slots"]["cell_ids"]["slot_uri"] = "CAS:has_cellid"
    if "cell_set_accession" in schema_obj["slots"]:
        schema_obj["slots"]["cell_set_accession"]["identifier"] = True
        # if "Bican_Annotation" in schema_obj["classes"] and \
        #         "attributes" in schema_obj["classes"]["Bican_Annotation"] and \
        #         "cell_set_accession" in schema_obj["classes"]["Bican_Annotation"]["attributes"]:
        #     schema_obj["classes"]["Bican_Annotation"]["attributes"]["cell_set_accession"]["identifier"] = True
    if "parent_cell_set_accession" in schema_obj["slots"]:
        # schema_obj["slots"]["parent_cell_set_accession"]["slot_uri"] = "RO:0015003"
        schema_obj["slots"]["parent_cell_set_accession"]["range"] = "Bican_Annotation"  # TODO
    # schema_obj["slots"]["source_taxonomy"]["range"] = "uriorcurie"
    # schema_obj["slots"]["comment"]["slot_uri"] = "IAO:0000115"
    # schema_obj["slots"]["labelset"]["slot_uri"] = "CAS:has_labelset"
    if "labelset" in schema_obj["slots"]:
        schema_obj["slots"]["labelset"]["range"] = "Bican_Labelset"   # TODO
    # schema_obj["slots"]["labelsets"]["inlined"] = True
    # schema_obj["slots"]["annotations"]["inlined"] = True
    # schema_obj["slots"]["cell_id"]["identifier"] = True   # TODO
    schema_obj["classes"]["Labelset"]["slots"] = list(schema_obj["classes"]["Labelset"]["slots"]) + ["id"]
    schema_obj["classes"]["Taxonomy"]["slots"] = list(schema_obj["classes"]["Taxonomy"]["slots"]) + ["id"]
    # this is a workaround for lack of annotation ids in the base schema
    taxonomy_slots = list(schema_obj["classes"]["Taxonomy"]["slots"])
    taxonomy_slots.remove("annotations")
    schema_obj["classes"]["Taxonomy"]["slots"] = taxonomy_slots
    bican_annotation_slots = schema_obj["classes"]["Bican_Taxonomy"].get("slots", list())
    bican_annotation_slots.append("annotations")
    schema_obj["classes"]["Bican_Taxonomy"]["slots"] = bican_annotation_slots

    # schema_obj["classes"]["Annotation"]["class_uri"] = "PCL:0010001"

    for class_name in schema_obj["classes"]:
        if "attributes" in schema_obj["classes"][class_name]:
            clazz = schema_obj["classes"][class_name]
            del clazz["attributes"]

    if output_path:
        write_schema(schema_obj, output_path)

    return schema_obj


def expand_schema(
    config: Optional[str],
    yaml_obj: dict,
    value_set_names: List[str],
    output_path: Optional[str] = None,
):
    """
    Dynamically expands the yaml_obj schema in-place using specified value set names.
    Args:
        config (Optional[str]): Path to the configuration file. If None, a default configuration is used.
        yaml_obj (dict): YAML schema object that will be expanded.
        value_set_names (List[str]): Names of the value sets to be included in the expansion.
        output_path (Optional[str]): Path where the expanded schema file will be saved, if specified.
    Note:
        Source code referenced from: https://github.com/INCATools/ontology-access-kit/blob/main/src/oaklib/utilities/subsets/value_set_expander.py
    """
    expander = ValueSetExpander()
    if config:
        expander.configuration = yaml_loader.load(
            config, target_class=ValueSetConfiguration
        )

    yaml = YAML()
    schema = yaml_loader.load(yaml_obj, target_class=SchemaDefinition)
    if value_set_names is None:
        value_set_names = list(schema.enums.keys())
    for value_set_name in value_set_names:
        if value_set_name not in schema.enums:
            raise ValueError(f"Unknown value set: {value_set_name}")
        value_set = schema.enums[value_set_name]
        pvs = list(expander.expand_value_set(value_set, schema=schema))
        yaml_obj["enums"][value_set_name]["permissible_values"] = {
            str(pv.text): json_dumper.to_dict(pv) for pv in pvs
        }
    if output_path:
        with open(output_path, "w", encoding="UTF-8") as file:
            yaml.dump(yaml_obj, stream=file)
    return yaml_obj
