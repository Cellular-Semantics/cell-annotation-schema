# Auto generated from BICAN_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-16T15:58:26
# Schema: General_Cell_Annotation_Open_Standard
#
# id: https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard
# description: General, open-standard schema for cell annotations
# license: GNU GPL v3.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CAS = CurieNamespace('CAS', 'https://w3id.org/Cellular-Semantics/cell-annotation-schema/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
PCL = CurieNamespace('PCL', 'http://purl.obolibrary.org/obo/PCL_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
CELL_ANNOTATION_SCHEMA = CurieNamespace('cell_annotation_schema', 'https://w3id.org/Cellular-Semantics/cell-annotation-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/')


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/String")


class Integer(int):
    """ An integer """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Integer")


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD["boolean"]
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Boolean")


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Float")


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Double")


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Decimal")


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD["time"]
    type_class_curie = "xsd:time"
    type_name = "time"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Time")


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Date")


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Datetime")


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML["DateOrDatetime"]
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/DateOrDatetime")


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Uriorcurie")


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Curie")


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Uri")


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Ncname")


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX["iri"]
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Objectidentifier")


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX["nonLiteral"]
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Nodeidentifier")


class Jsonpointer(str):
    """ A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpointer"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Jsonpointer")


class Jsonpath(str):
    """ A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpath"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Jsonpath")


class Sparqlpath(str):
    """ A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sparqlpath"
    type_model_uri = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Sparqlpath")


# Class references



@dataclass
class AnnotationTransfer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/AnnotationTransfer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnnotationTransfer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/AnnotationTransfer")

    transferred_cell_label: Optional[str] = None
    source_taxonomy: Optional[Union[str, URIorCURIE]] = None
    source_node_accession: Optional[str] = None
    algorithm_name: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transferred_cell_label is not None and not isinstance(self.transferred_cell_label, str):
            self.transferred_cell_label = str(self.transferred_cell_label)

        if self.source_taxonomy is not None and not isinstance(self.source_taxonomy, URIorCURIE):
            self.source_taxonomy = URIorCURIE(self.source_taxonomy)

        if self.source_node_accession is not None and not isinstance(self.source_node_accession, str):
            self.source_node_accession = str(self.source_node_accession)

        if self.algorithm_name is not None and not isinstance(self.algorithm_name, str):
            self.algorithm_name = str(self.algorithm_name)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.transferred_cell_label is not None and not isinstance(self.transferred_cell_label, str):
            self.transferred_cell_label = str(self.transferred_cell_label)

        if self.source_taxonomy is not None and not isinstance(self.source_taxonomy, URIorCURIE):
            self.source_taxonomy = URIorCURIE(self.source_taxonomy)

        if self.source_node_accession is not None and not isinstance(self.source_node_accession, str):
            self.source_node_accession = str(self.source_node_accession)

        if self.algorithm_name is not None and not isinstance(self.algorithm_name, str):
            self.algorithm_name = str(self.algorithm_name)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass
class Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Cell")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Cell"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Cell")

    cell_id: str = None
    confidence: Optional[float] = None
    author_categories: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_id):
            self.MissingRequiredField("cell_id")
        if not isinstance(self.cell_id, str):
            self.cell_id = str(self.cell_id)

        if self._is_empty(self.cell_id):
            self.MissingRequiredField("cell_id")
        if not isinstance(self.cell_id, str):
            self.cell_id = str(self.cell_id)

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if self.author_categories is not None and not isinstance(self.author_categories, str):
            self.author_categories = str(self.author_categories)

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if self.author_categories is not None and not isinstance(self.author_categories, str):
            self.author_categories = str(self.author_categories)

        super().__post_init__(**kwargs)


@dataclass
class Review(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Review")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Review"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Review")

    datestamp: str = None
    reviewer: Optional[str] = None
    review: Optional[Union[str, "ReviewOptions"]] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.datestamp):
            self.MissingRequiredField("datestamp")
        if not isinstance(self.datestamp, str):
            self.datestamp = str(self.datestamp)

        if self._is_empty(self.datestamp):
            self.MissingRequiredField("datestamp")
        if not isinstance(self.datestamp, str):
            self.datestamp = str(self.datestamp)

        if self.reviewer is not None and not isinstance(self.reviewer, str):
            self.reviewer = str(self.reviewer)

        if self.review is not None and not isinstance(self.review, ReviewOptions):
            self.review = ReviewOptions(self.review)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self.reviewer is not None and not isinstance(self.reviewer, str):
            self.reviewer = str(self.reviewer)

        if self.review is not None and not isinstance(self.review, ReviewOptions):
            self.review = ReviewOptions(self.review)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        super().__post_init__(**kwargs)


@dataclass
class Labelset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Labelset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Labelset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Labelset")

    name: str = None
    description: Optional[str] = None
    annotation_method: Optional[Union[str, "AnnotationMethodOptions"]] = None
    automated_annotation: Optional[Union[dict, "AutomatedAnnotation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.annotation_method is not None and not isinstance(self.annotation_method, AnnotationMethodOptions):
            self.annotation_method = AnnotationMethodOptions(self.annotation_method)

        if self.automated_annotation is not None and not isinstance(self.automated_annotation, AutomatedAnnotation):
            self.automated_annotation = AutomatedAnnotation(**as_dict(self.automated_annotation))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.annotation_method is not None and not isinstance(self.annotation_method, AnnotationMethodOptions):
            self.annotation_method = AnnotationMethodOptions(self.annotation_method)

        if self.automated_annotation is not None and not isinstance(self.automated_annotation, AutomatedAnnotation):
            self.automated_annotation = AutomatedAnnotation(**as_dict(self.automated_annotation))

        super().__post_init__(**kwargs)


@dataclass
class BicanLabelset(Labelset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/BicanLabelset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Bican_Labelset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/BicanLabelset")

    name: str = None
    rank: Optional[int] = None
    description: Optional[str] = None
    annotation_method: Optional[Union[str, "AnnotationMethodOptions"]] = None
    automated_annotation: Optional[Union[dict, "AutomatedAnnotation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.rank is not None and not isinstance(self.rank, int):
            self.rank = int(self.rank)

        if self.rank is not None and not isinstance(self.rank, int):
            self.rank = int(self.rank)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.annotation_method is not None and not isinstance(self.annotation_method, AnnotationMethodOptions):
            self.annotation_method = AnnotationMethodOptions(self.annotation_method)

        if self.automated_annotation is not None and not isinstance(self.automated_annotation, AutomatedAnnotation):
            self.automated_annotation = AutomatedAnnotation(**as_dict(self.automated_annotation))

        super().__post_init__(**kwargs)


@dataclass
class AutomatedAnnotation(YAMLRoot):
    """
    A set of fields for recording the details of the automated annotation algorithm used. (Common 'automated
    annotation methods' would include PopV, Azimuth, CellTypist, scArches, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/AutomatedAnnotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AutomatedAnnotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/AutomatedAnnotation")

    algorithm_version: str = None
    algorithm_repo_url: str = None
    algorithm_name: Optional[str] = None
    reference_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.algorithm_version):
            self.MissingRequiredField("algorithm_version")
        if not isinstance(self.algorithm_version, str):
            self.algorithm_version = str(self.algorithm_version)

        if self._is_empty(self.algorithm_repo_url):
            self.MissingRequiredField("algorithm_repo_url")
        if not isinstance(self.algorithm_repo_url, str):
            self.algorithm_repo_url = str(self.algorithm_repo_url)

        if self._is_empty(self.algorithm_version):
            self.MissingRequiredField("algorithm_version")
        if not isinstance(self.algorithm_version, str):
            self.algorithm_version = str(self.algorithm_version)

        if self._is_empty(self.algorithm_repo_url):
            self.MissingRequiredField("algorithm_repo_url")
        if not isinstance(self.algorithm_repo_url, str):
            self.algorithm_repo_url = str(self.algorithm_repo_url)

        if self.algorithm_name is not None and not isinstance(self.algorithm_name, str):
            self.algorithm_name = str(self.algorithm_name)

        if self.reference_location is not None and not isinstance(self.reference_location, str):
            self.reference_location = str(self.reference_location)

        if self.algorithm_name is not None and not isinstance(self.algorithm_name, str):
            self.algorithm_name = str(self.algorithm_name)

        if self.reference_location is not None and not isinstance(self.reference_location, str):
            self.reference_location = str(self.reference_location)

        super().__post_init__(**kwargs)


@dataclass
class Annotation(YAMLRoot):
    """
    A collection of fields recording a cell type/class/state annotation on some set of cells, supporting evidence and
    provenance. As this is intended as a general schema, compulsory fields are kept to a minimum. However, tools using
    this schema are encouarged to specify a larger set of compulsory fields for publication. Note: This schema
    deliberately allows for additional fields in order to support ad hoc user fields, new formal schema extensions and
    project/tool specific metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Annotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Annotation")

    labelset: str = None
    cell_label: str = None
    cell_fullname: Optional[str] = None
    cell_ontology_term_id: Optional[Union[str, "CellTypeEnum"]] = None
    cell_ontology_term: Optional[str] = None
    cell_ids: Optional[Union[str, List[str]]] = empty_list()
    rationale: Optional[str] = None
    rationale_dois: Optional[Union[str, List[str]]] = empty_list()
    marker_gene_evidence: Optional[Union[str, List[str]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    reviews: Optional[Union[Union[dict, Review], List[Union[dict, Review]]]] = empty_list()
    author_annotation_fields: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.labelset):
            self.MissingRequiredField("labelset")
        if not isinstance(self.labelset, str):
            self.labelset = str(self.labelset)

        if self._is_empty(self.cell_label):
            self.MissingRequiredField("cell_label")
        if not isinstance(self.cell_label, str):
            self.cell_label = str(self.cell_label)

        if self._is_empty(self.labelset):
            self.MissingRequiredField("labelset")
        if not isinstance(self.labelset, str):
            self.labelset = str(self.labelset)

        if self._is_empty(self.cell_label):
            self.MissingRequiredField("cell_label")
        if not isinstance(self.cell_label, str):
            self.cell_label = str(self.cell_label)

        if self.cell_fullname is not None and not isinstance(self.cell_fullname, str):
            self.cell_fullname = str(self.cell_fullname)

        if self.cell_ontology_term is not None and not isinstance(self.cell_ontology_term, str):
            self.cell_ontology_term = str(self.cell_ontology_term)

        if not isinstance(self.cell_ids, list):
            self.cell_ids = [self.cell_ids] if self.cell_ids is not None else []
        self.cell_ids = [v if isinstance(v, str) else str(v) for v in self.cell_ids]

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.rationale_dois, list):
            self.rationale_dois = [self.rationale_dois] if self.rationale_dois is not None else []
        self.rationale_dois = [v if isinstance(v, str) else str(v) for v in self.rationale_dois]

        if not isinstance(self.marker_gene_evidence, list):
            self.marker_gene_evidence = [self.marker_gene_evidence] if self.marker_gene_evidence is not None else []
        self.marker_gene_evidence = [v if isinstance(v, str) else str(v) for v in self.marker_gene_evidence]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_dict(slot_name="reviews", slot_type=Review, key_name="datestamp", keyed=False)

        if self.author_annotation_fields is not None and not isinstance(self.author_annotation_fields, str):
            self.author_annotation_fields = str(self.author_annotation_fields)

        if self.cell_fullname is not None and not isinstance(self.cell_fullname, str):
            self.cell_fullname = str(self.cell_fullname)

        if self.cell_ontology_term is not None and not isinstance(self.cell_ontology_term, str):
            self.cell_ontology_term = str(self.cell_ontology_term)

        if not isinstance(self.cell_ids, list):
            self.cell_ids = [self.cell_ids] if self.cell_ids is not None else []
        self.cell_ids = [v if isinstance(v, str) else str(v) for v in self.cell_ids]

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.rationale_dois, list):
            self.rationale_dois = [self.rationale_dois] if self.rationale_dois is not None else []
        self.rationale_dois = [v if isinstance(v, str) else str(v) for v in self.rationale_dois]

        if not isinstance(self.marker_gene_evidence, list):
            self.marker_gene_evidence = [self.marker_gene_evidence] if self.marker_gene_evidence is not None else []
        self.marker_gene_evidence = [v if isinstance(v, str) else str(v) for v in self.marker_gene_evidence]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_dict(slot_name="reviews", slot_type=Review, key_name="datestamp", keyed=False)

        if self.author_annotation_fields is not None and not isinstance(self.author_annotation_fields, str):
            self.author_annotation_fields = str(self.author_annotation_fields)

        super().__post_init__(**kwargs)


@dataclass
class BicanAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/BicanAnnotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Bican_Annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/BicanAnnotation")

    labelset: str = None
    cell_label: str = None
    cell_set_accession: Optional[str] = None
    parent_cell_set_accession: Optional[str] = None
    transferred_annotations: Optional[Union[Union[dict, AnnotationTransfer], List[Union[dict, AnnotationTransfer]]]] = empty_list()
    cells: Optional[Union[Union[dict, Cell], List[Union[dict, Cell]]]] = empty_list()
    negative_marker_gene_evidence: Optional[Union[str, List[str]]] = empty_list()
    cell_fullname: Optional[str] = None
    cell_ontology_term_id: Optional[Union[str, "CellTypeEnum"]] = None
    cell_ontology_term: Optional[str] = None
    cell_ids: Optional[Union[str, List[str]]] = empty_list()
    rationale: Optional[str] = None
    rationale_dois: Optional[Union[str, List[str]]] = empty_list()
    marker_gene_evidence: Optional[Union[str, List[str]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    reviews: Optional[Union[Union[dict, Review], List[Union[dict, Review]]]] = empty_list()
    author_annotation_fields: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.labelset):
            self.MissingRequiredField("labelset")
        if not isinstance(self.labelset, str):
            self.labelset = str(self.labelset)

        if self._is_empty(self.cell_label):
            self.MissingRequiredField("cell_label")
        if not isinstance(self.cell_label, str):
            self.cell_label = str(self.cell_label)

        if self.cell_set_accession is not None and not isinstance(self.cell_set_accession, str):
            self.cell_set_accession = str(self.cell_set_accession)

        if self.parent_cell_set_accession is not None and not isinstance(self.parent_cell_set_accession, str):
            self.parent_cell_set_accession = str(self.parent_cell_set_accession)

        if not isinstance(self.transferred_annotations, list):
            self.transferred_annotations = [self.transferred_annotations] if self.transferred_annotations is not None else []
        self.transferred_annotations = [v if isinstance(v, AnnotationTransfer) else AnnotationTransfer(**as_dict(v)) for v in self.transferred_annotations]

        self._normalize_inlined_as_dict(slot_name="cells", slot_type=Cell, key_name="cell_id", keyed=False)

        if not isinstance(self.negative_marker_gene_evidence, list):
            self.negative_marker_gene_evidence = [self.negative_marker_gene_evidence] if self.negative_marker_gene_evidence is not None else []
        self.negative_marker_gene_evidence = [v if isinstance(v, str) else str(v) for v in self.negative_marker_gene_evidence]

        if self.cell_set_accession is not None and not isinstance(self.cell_set_accession, str):
            self.cell_set_accession = str(self.cell_set_accession)

        if self.parent_cell_set_accession is not None and not isinstance(self.parent_cell_set_accession, str):
            self.parent_cell_set_accession = str(self.parent_cell_set_accession)

        if not isinstance(self.transferred_annotations, list):
            self.transferred_annotations = [self.transferred_annotations] if self.transferred_annotations is not None else []
        self.transferred_annotations = [v if isinstance(v, AnnotationTransfer) else AnnotationTransfer(**as_dict(v)) for v in self.transferred_annotations]

        self._normalize_inlined_as_dict(slot_name="cells", slot_type=Cell, key_name="cell_id", keyed=False)

        if not isinstance(self.negative_marker_gene_evidence, list):
            self.negative_marker_gene_evidence = [self.negative_marker_gene_evidence] if self.negative_marker_gene_evidence is not None else []
        self.negative_marker_gene_evidence = [v if isinstance(v, str) else str(v) for v in self.negative_marker_gene_evidence]

        if self.cell_fullname is not None and not isinstance(self.cell_fullname, str):
            self.cell_fullname = str(self.cell_fullname)

        if self.cell_ontology_term is not None and not isinstance(self.cell_ontology_term, str):
            self.cell_ontology_term = str(self.cell_ontology_term)

        if not isinstance(self.cell_ids, list):
            self.cell_ids = [self.cell_ids] if self.cell_ids is not None else []
        self.cell_ids = [v if isinstance(v, str) else str(v) for v in self.cell_ids]

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.rationale_dois, list):
            self.rationale_dois = [self.rationale_dois] if self.rationale_dois is not None else []
        self.rationale_dois = [v if isinstance(v, str) else str(v) for v in self.rationale_dois]

        if not isinstance(self.marker_gene_evidence, list):
            self.marker_gene_evidence = [self.marker_gene_evidence] if self.marker_gene_evidence is not None else []
        self.marker_gene_evidence = [v if isinstance(v, str) else str(v) for v in self.marker_gene_evidence]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_dict(slot_name="reviews", slot_type=Review, key_name="datestamp", keyed=False)

        if self.author_annotation_fields is not None and not isinstance(self.author_annotation_fields, str):
            self.author_annotation_fields = str(self.author_annotation_fields)

        super().__post_init__(**kwargs)


@dataclass
class Taxonomy(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Taxonomy")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Taxonomy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/Taxonomy")

    title: str = None
    author_name: str = None
    labelsets: Union[Union[dict, Labelset], List[Union[dict, Labelset]]] = None
    annotations: Union[Union[dict, Annotation], List[Union[dict, Annotation]]] = None
    matrix_file_id: Optional[str] = None
    description: Optional[str] = None
    cellannotation_schema_version: Optional[str] = None
    cellannotation_timestamp: Optional[str] = None
    cellannotation_version: Optional[str] = None
    cellannotation_url: Optional[str] = None
    author_list: Optional[str] = None
    author_contact: Optional[str] = None
    orcid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.author_name):
            self.MissingRequiredField("author_name")
        if not isinstance(self.author_name, str):
            self.author_name = str(self.author_name)

        if self._is_empty(self.labelsets):
            self.MissingRequiredField("labelsets")
        self._normalize_inlined_as_dict(slot_name="labelsets", slot_type=Labelset, key_name="name", keyed=False)

        if self._is_empty(self.annotations):
            self.MissingRequiredField("annotations")
        self._normalize_inlined_as_dict(slot_name="annotations", slot_type=Annotation, key_name="labelset", keyed=False)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.author_name):
            self.MissingRequiredField("author_name")
        if not isinstance(self.author_name, str):
            self.author_name = str(self.author_name)

        if self._is_empty(self.labelsets):
            self.MissingRequiredField("labelsets")
        self._normalize_inlined_as_dict(slot_name="labelsets", slot_type=Labelset, key_name="name", keyed=False)

        if self._is_empty(self.annotations):
            self.MissingRequiredField("annotations")
        self._normalize_inlined_as_dict(slot_name="annotations", slot_type=Annotation, key_name="labelset", keyed=False)

        if self.matrix_file_id is not None and not isinstance(self.matrix_file_id, str):
            self.matrix_file_id = str(self.matrix_file_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.cellannotation_schema_version is not None and not isinstance(self.cellannotation_schema_version, str):
            self.cellannotation_schema_version = str(self.cellannotation_schema_version)

        if self.cellannotation_timestamp is not None and not isinstance(self.cellannotation_timestamp, str):
            self.cellannotation_timestamp = str(self.cellannotation_timestamp)

        if self.cellannotation_version is not None and not isinstance(self.cellannotation_version, str):
            self.cellannotation_version = str(self.cellannotation_version)

        if self.cellannotation_url is not None and not isinstance(self.cellannotation_url, str):
            self.cellannotation_url = str(self.cellannotation_url)

        if self.author_list is not None and not isinstance(self.author_list, str):
            self.author_list = str(self.author_list)

        if self.author_contact is not None and not isinstance(self.author_contact, str):
            self.author_contact = str(self.author_contact)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.matrix_file_id is not None and not isinstance(self.matrix_file_id, str):
            self.matrix_file_id = str(self.matrix_file_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.cellannotation_schema_version is not None and not isinstance(self.cellannotation_schema_version, str):
            self.cellannotation_schema_version = str(self.cellannotation_schema_version)

        if self.cellannotation_timestamp is not None and not isinstance(self.cellannotation_timestamp, str):
            self.cellannotation_timestamp = str(self.cellannotation_timestamp)

        if self.cellannotation_version is not None and not isinstance(self.cellannotation_version, str):
            self.cellannotation_version = str(self.cellannotation_version)

        if self.cellannotation_url is not None and not isinstance(self.cellannotation_url, str):
            self.cellannotation_url = str(self.cellannotation_url)

        if self.author_list is not None and not isinstance(self.author_list, str):
            self.author_list = str(self.author_list)

        if self.author_contact is not None and not isinstance(self.author_contact, str):
            self.author_contact = str(self.author_contact)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        super().__post_init__(**kwargs)


@dataclass
class BicanTaxonomy(Taxonomy):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/BicanTaxonomy")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Bican_Taxonomy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/Cellular-Semantics/General-Cell-Annotation-Open-Standard/BicanTaxonomy")

    title: str = None
    author_name: str = None
    labelsets: Union[Union[dict, BicanLabelset], List[Union[dict, BicanLabelset]]] = None
    annotations: Union[Union[dict, BicanAnnotation], List[Union[dict, BicanAnnotation]]] = None
    matrix_file_id: Optional[str] = None
    description: Optional[str] = None
    cellannotation_schema_version: Optional[str] = None
    cellannotation_timestamp: Optional[str] = None
    cellannotation_version: Optional[str] = None
    cellannotation_url: Optional[str] = None
    author_list: Optional[str] = None
    author_contact: Optional[str] = None
    orcid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.author_name):
            self.MissingRequiredField("author_name")
        if not isinstance(self.author_name, str):
            self.author_name = str(self.author_name)

        if self._is_empty(self.labelsets):
            self.MissingRequiredField("labelsets")
        self._normalize_inlined_as_dict(slot_name="labelsets", slot_type=BicanLabelset, key_name="name", keyed=False)

        if self._is_empty(self.annotations):
            self.MissingRequiredField("annotations")
        self._normalize_inlined_as_dict(slot_name="annotations", slot_type=BicanAnnotation, key_name="labelset", keyed=False)

        if self._is_empty(self.labelsets):
            self.MissingRequiredField("labelsets")
        self._normalize_inlined_as_dict(slot_name="labelsets", slot_type=BicanLabelset, key_name="name", keyed=False)

        if self._is_empty(self.annotations):
            self.MissingRequiredField("annotations")
        self._normalize_inlined_as_dict(slot_name="annotations", slot_type=BicanAnnotation, key_name="labelset", keyed=False)

        if self.matrix_file_id is not None and not isinstance(self.matrix_file_id, str):
            self.matrix_file_id = str(self.matrix_file_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.cellannotation_schema_version is not None and not isinstance(self.cellannotation_schema_version, str):
            self.cellannotation_schema_version = str(self.cellannotation_schema_version)

        if self.cellannotation_timestamp is not None and not isinstance(self.cellannotation_timestamp, str):
            self.cellannotation_timestamp = str(self.cellannotation_timestamp)

        if self.cellannotation_version is not None and not isinstance(self.cellannotation_version, str):
            self.cellannotation_version = str(self.cellannotation_version)

        if self.cellannotation_url is not None and not isinstance(self.cellannotation_url, str):
            self.cellannotation_url = str(self.cellannotation_url)

        if self.author_list is not None and not isinstance(self.author_list, str):
            self.author_list = str(self.author_list)

        if self.author_contact is not None and not isinstance(self.author_contact, str):
            self.author_contact = str(self.author_contact)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        super().__post_init__(**kwargs)


# Enumerations
class ReviewOptions(EnumDefinitionImpl):

    Agree = PermissibleValue(text="Agree")
    Disagree = PermissibleValue(text="Disagree")

    _defn = EnumDefinition(
        name="ReviewOptions",
    )

class AnnotationMethodOptions(EnumDefinitionImpl):

    algorithmic = PermissibleValue(text="algorithmic")
    manual = PermissibleValue(text="manual")
    both = PermissibleValue(text="both")

    _defn = EnumDefinition(
        name="AnnotationMethodOptions",
    )

class CellTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellTypeEnum",
    )

# Slots
