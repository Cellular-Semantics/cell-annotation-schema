# Auto generated from None by pythongen.py version: 0.0.1
# Generation date: 2024-07-31T16:21:54
# Schema: General_Cell_Annotation_Open_Standard
#
# id: https://cellular-semantics.sanger.ac.uk/ontology/CAS
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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CAS = CurieNamespace('CAS', 'https://cellular-semantics.sanger.ac.uk/ontology/CAS/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
PCL = CurieNamespace('PCL', 'http://purl.obolibrary.org/obo/PCL_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
CELL_ANNOTATION_SCHEMA = CurieNamespace('cell_annotation_schema', 'https://cellular-semantics.sanger.ac.uk/ontology/CAS/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = CELL_ANNOTATION_SCHEMA


# Types

# Class references



@dataclass
class Review(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA["Review"]
    class_class_curie: ClassVar[str] = "cell_annotation_schema:Review"
    class_name: ClassVar[str] = "Review"
    class_model_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA.Review

    datestamp: str = None
    reviewer: Optional[str] = None
    review: Optional[Union[str, "ReviewOptions"]] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        super().__post_init__(**kwargs)


@dataclass
class Labelset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA["Labelset"]
    class_class_curie: ClassVar[str] = "cell_annotation_schema:Labelset"
    class_name: ClassVar[str] = "Labelset"
    class_model_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA.Labelset

    name: str = None
    description: Optional[str] = None
    annotation_method: Optional[Union[str, "AnnotationMethodOptions"]] = None
    automated_annotation: Optional[Union[dict, "AutomatedAnnotation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        super().__post_init__(**kwargs)


@dataclass
class AutomatedAnnotation(YAMLRoot):
    """
    A set of fields for recording the details of the automated annotation algorithm used. (Common 'automated
    annotation methods' would include PopV, Azimuth, CellTypist, scArches, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA["AutomatedAnnotation"]
    class_class_curie: ClassVar[str] = "cell_annotation_schema:AutomatedAnnotation"
    class_name: ClassVar[str] = "AutomatedAnnotation"
    class_model_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA.AutomatedAnnotation

    algorithm_name: str = None
    algorithm_version: str = None
    algorithm_repo_url: str = None
    reference_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.algorithm_name):
            self.MissingRequiredField("algorithm_name")
        if not isinstance(self.algorithm_name, str):
            self.algorithm_name = str(self.algorithm_name)

        if self._is_empty(self.algorithm_version):
            self.MissingRequiredField("algorithm_version")
        if not isinstance(self.algorithm_version, str):
            self.algorithm_version = str(self.algorithm_version)

        if self._is_empty(self.algorithm_repo_url):
            self.MissingRequiredField("algorithm_repo_url")
        if not isinstance(self.algorithm_repo_url, str):
            self.algorithm_repo_url = str(self.algorithm_repo_url)

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

    class_class_uri: ClassVar[URIRef] = PCL["0010001"]
    class_class_curie: ClassVar[str] = "PCL:0010001"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA.Annotation

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

    class_class_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA["Taxonomy"]
    class_class_curie: ClassVar[str] = "cell_annotation_schema:Taxonomy"
    class_name: ClassVar[str] = "Taxonomy"
    class_model_uri: ClassVar[URIRef] = CELL_ANNOTATION_SCHEMA.Taxonomy

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
class slots:
    pass

slots.datestamp = Slot(uri=CELL_ANNOTATION_SCHEMA.datestamp, name="datestamp", curie=CELL_ANNOTATION_SCHEMA.curie('datestamp'),
                   model_uri=CELL_ANNOTATION_SCHEMA.datestamp, domain=None, range=str)

slots.reviewer = Slot(uri=CELL_ANNOTATION_SCHEMA.reviewer, name="reviewer", curie=CELL_ANNOTATION_SCHEMA.curie('reviewer'),
                   model_uri=CELL_ANNOTATION_SCHEMA.reviewer, domain=None, range=Optional[str])

slots.review = Slot(uri=CELL_ANNOTATION_SCHEMA.review, name="review", curie=CELL_ANNOTATION_SCHEMA.curie('review'),
                   model_uri=CELL_ANNOTATION_SCHEMA.review, domain=None, range=Optional[Union[str, "ReviewOptions"]])

slots.explanation = Slot(uri=IAO['0000115'], name="explanation", curie=IAO.curie('0000115'),
                   model_uri=CELL_ANNOTATION_SCHEMA.explanation, domain=None, range=Optional[str])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CELL_ANNOTATION_SCHEMA.name, domain=None, range=str)

slots.description = Slot(uri=IAO['0000115'], name="description", curie=IAO.curie('0000115'),
                   model_uri=CELL_ANNOTATION_SCHEMA.description, domain=None, range=Optional[str])

slots.annotation_method = Slot(uri=CELL_ANNOTATION_SCHEMA.annotation_method, name="annotation_method", curie=CELL_ANNOTATION_SCHEMA.curie('annotation_method'),
                   model_uri=CELL_ANNOTATION_SCHEMA.annotation_method, domain=None, range=Optional[Union[str, "AnnotationMethodOptions"]])

slots.automated_annotation = Slot(uri=CELL_ANNOTATION_SCHEMA.automated_annotation, name="automated_annotation", curie=CELL_ANNOTATION_SCHEMA.curie('automated_annotation'),
                   model_uri=CELL_ANNOTATION_SCHEMA.automated_annotation, domain=None, range=Optional[Union[dict, AutomatedAnnotation]])

slots.algorithm_name = Slot(uri=CELL_ANNOTATION_SCHEMA.algorithm_name, name="algorithm_name", curie=CELL_ANNOTATION_SCHEMA.curie('algorithm_name'),
                   model_uri=CELL_ANNOTATION_SCHEMA.algorithm_name, domain=None, range=str)

slots.algorithm_version = Slot(uri=CELL_ANNOTATION_SCHEMA.algorithm_version, name="algorithm_version", curie=CELL_ANNOTATION_SCHEMA.curie('algorithm_version'),
                   model_uri=CELL_ANNOTATION_SCHEMA.algorithm_version, domain=None, range=str)

slots.algorithm_repo_url = Slot(uri=CELL_ANNOTATION_SCHEMA.algorithm_repo_url, name="algorithm_repo_url", curie=CELL_ANNOTATION_SCHEMA.curie('algorithm_repo_url'),
                   model_uri=CELL_ANNOTATION_SCHEMA.algorithm_repo_url, domain=None, range=str)

slots.reference_location = Slot(uri=CELL_ANNOTATION_SCHEMA.reference_location, name="reference_location", curie=CELL_ANNOTATION_SCHEMA.curie('reference_location'),
                   model_uri=CELL_ANNOTATION_SCHEMA.reference_location, domain=None, range=Optional[str])

slots.labelset = Slot(uri=CAS.has_labelset, name="labelset", curie=CAS.curie('has_labelset'),
                   model_uri=CELL_ANNOTATION_SCHEMA.labelset, domain=None, range=str)

slots.cell_label = Slot(uri=RDFS.label, name="cell_label", curie=RDFS.curie('label'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cell_label, domain=None, range=str)

slots.cell_fullname = Slot(uri=SKOS.preflabel, name="cell_fullname", curie=SKOS.curie('preflabel'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cell_fullname, domain=None, range=Optional[str])

slots.cell_ontology_term_id = Slot(uri=RO['0002473'], name="cell_ontology_term_id", curie=RO.curie('0002473'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cell_ontology_term_id, domain=None, range=Optional[Union[str, "CellTypeEnum"]])

slots.cell_ontology_term = Slot(uri=CELL_ANNOTATION_SCHEMA.cell_ontology_term, name="cell_ontology_term", curie=CELL_ANNOTATION_SCHEMA.curie('cell_ontology_term'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cell_ontology_term, domain=None, range=Optional[str])

slots.cell_ids = Slot(uri=CAS.has_cellid, name="cell_ids", curie=CAS.curie('has_cellid'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cell_ids, domain=None, range=Optional[Union[str, List[str]]])

slots.rationale = Slot(uri=CELL_ANNOTATION_SCHEMA.rationale, name="rationale", curie=CELL_ANNOTATION_SCHEMA.curie('rationale'),
                   model_uri=CELL_ANNOTATION_SCHEMA.rationale, domain=None, range=Optional[str])

slots.rationale_dois = Slot(uri=CELL_ANNOTATION_SCHEMA.rationale_dois, name="rationale_dois", curie=CELL_ANNOTATION_SCHEMA.curie('rationale_dois'),
                   model_uri=CELL_ANNOTATION_SCHEMA.rationale_dois, domain=None, range=Optional[Union[str, List[str]]])

slots.marker_gene_evidence = Slot(uri=CELL_ANNOTATION_SCHEMA.marker_gene_evidence, name="marker_gene_evidence", curie=CELL_ANNOTATION_SCHEMA.curie('marker_gene_evidence'),
                   model_uri=CELL_ANNOTATION_SCHEMA.marker_gene_evidence, domain=None, range=Optional[Union[str, List[str]]])

slots.synonyms = Slot(uri=CELL_ANNOTATION_SCHEMA.synonyms, name="synonyms", curie=CELL_ANNOTATION_SCHEMA.curie('synonyms'),
                   model_uri=CELL_ANNOTATION_SCHEMA.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.reviews = Slot(uri=CELL_ANNOTATION_SCHEMA.reviews, name="reviews", curie=CELL_ANNOTATION_SCHEMA.curie('reviews'),
                   model_uri=CELL_ANNOTATION_SCHEMA.reviews, domain=None, range=Optional[Union[Union[dict, Review], List[Union[dict, Review]]]])

slots.author_annotation_fields = Slot(uri=CELL_ANNOTATION_SCHEMA.author_annotation_fields, name="author_annotation_fields", curie=CELL_ANNOTATION_SCHEMA.curie('author_annotation_fields'),
                   model_uri=CELL_ANNOTATION_SCHEMA.author_annotation_fields, domain=None, range=Optional[str])

slots.matrix_file_id = Slot(uri=CELL_ANNOTATION_SCHEMA.matrix_file_id, name="matrix_file_id", curie=CELL_ANNOTATION_SCHEMA.curie('matrix_file_id'),
                   model_uri=CELL_ANNOTATION_SCHEMA.matrix_file_id, domain=None, range=Optional[str])

slots.title = Slot(uri=CELL_ANNOTATION_SCHEMA.title, name="title", curie=CELL_ANNOTATION_SCHEMA.curie('title'),
                   model_uri=CELL_ANNOTATION_SCHEMA.title, domain=None, range=str)

slots.cellannotation_schema_version = Slot(uri=CELL_ANNOTATION_SCHEMA.cellannotation_schema_version, name="cellannotation_schema_version", curie=CELL_ANNOTATION_SCHEMA.curie('cellannotation_schema_version'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cellannotation_schema_version, domain=None, range=Optional[str])

slots.cellannotation_timestamp = Slot(uri=CELL_ANNOTATION_SCHEMA.cellannotation_timestamp, name="cellannotation_timestamp", curie=CELL_ANNOTATION_SCHEMA.curie('cellannotation_timestamp'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cellannotation_timestamp, domain=None, range=Optional[str])

slots.cellannotation_version = Slot(uri=CELL_ANNOTATION_SCHEMA.cellannotation_version, name="cellannotation_version", curie=CELL_ANNOTATION_SCHEMA.curie('cellannotation_version'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cellannotation_version, domain=None, range=Optional[str])

slots.cellannotation_url = Slot(uri=CELL_ANNOTATION_SCHEMA.cellannotation_url, name="cellannotation_url", curie=CELL_ANNOTATION_SCHEMA.curie('cellannotation_url'),
                   model_uri=CELL_ANNOTATION_SCHEMA.cellannotation_url, domain=None, range=Optional[str])

slots.author_list = Slot(uri=CELL_ANNOTATION_SCHEMA.author_list, name="author_list", curie=CELL_ANNOTATION_SCHEMA.curie('author_list'),
                   model_uri=CELL_ANNOTATION_SCHEMA.author_list, domain=None, range=Optional[str])

slots.author_name = Slot(uri=CELL_ANNOTATION_SCHEMA.author_name, name="author_name", curie=CELL_ANNOTATION_SCHEMA.curie('author_name'),
                   model_uri=CELL_ANNOTATION_SCHEMA.author_name, domain=None, range=str)

slots.author_contact = Slot(uri=CELL_ANNOTATION_SCHEMA.author_contact, name="author_contact", curie=CELL_ANNOTATION_SCHEMA.curie('author_contact'),
                   model_uri=CELL_ANNOTATION_SCHEMA.author_contact, domain=None, range=Optional[str])

slots.orcid = Slot(uri=CELL_ANNOTATION_SCHEMA.orcid, name="orcid", curie=CELL_ANNOTATION_SCHEMA.curie('orcid'),
                   model_uri=CELL_ANNOTATION_SCHEMA.orcid, domain=None, range=Optional[str])

slots.labelsets = Slot(uri=CELL_ANNOTATION_SCHEMA.labelsets, name="labelsets", curie=CELL_ANNOTATION_SCHEMA.curie('labelsets'),
                   model_uri=CELL_ANNOTATION_SCHEMA.labelsets, domain=None, range=Union[Union[dict, Labelset], List[Union[dict, Labelset]]])

slots.annotations = Slot(uri=CELL_ANNOTATION_SCHEMA.annotations, name="annotations", curie=CELL_ANNOTATION_SCHEMA.curie('annotations'),
                   model_uri=CELL_ANNOTATION_SCHEMA.annotations, domain=None, range=Union[Union[dict, Annotation], List[Union[dict, Annotation]]])

slots.id = Slot(uri=CELL_ANNOTATION_SCHEMA.id, name="id", curie=CELL_ANNOTATION_SCHEMA.curie('id'),
                   model_uri=CELL_ANNOTATION_SCHEMA.id, domain=None, range=URIRef)