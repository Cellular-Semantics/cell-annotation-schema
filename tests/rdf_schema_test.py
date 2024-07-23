import os
import unittest

from cell_annotation_schema.file_utils import read_schema
from cell_annotation_schema.ontology.schema import (
    decorate_linkml_schema,
    expand_schema,
)


TESTDATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "../test_data/linkml/"
)

RAW_LINKML_SCHEMA = os.path.join(TESTDATA, "BICAN-schema-raw.yaml")


class LinkMLSchemaCase(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile(RAW_LINKML_SCHEMA):
            os.remove(RAW_LINKML_SCHEMA)

    def test_decorate_linkml_schema(self):
        bican_linkml_schema = read_schema("bican")
        decorated_schema = decorate_linkml_schema(
            bican_linkml_schema,
            ontology_namespace="MTG",
            ontology_iri="https://purl.brain-bican.org/ontology/AIT_MTG/",
            labelsets=["CrossArea_cluster", "CrossArea_subclass", "Class"],
        )
        self.assertIsNotNone(decorated_schema)

        self.assertEqual(
            "General_Cell_Annotation_Open_Standard", decorated_schema["name"]
        )
        self.assertTrue(len(decorated_schema["classes"]) >= 10)
        self.assertTrue(len(decorated_schema["slots"]) >= 50)
        self.assertTrue(len(decorated_schema["prefixes"]) >= 16)

    def test_expand_schema(self):
        bican_linkml_schema = read_schema("bican")
        decorated_schema = decorate_linkml_schema(
            bican_linkml_schema,
            ontology_namespace="MTG",
            ontology_iri="https://purl.brain-bican.org/ontology/AIT_MTG/",
            labelsets=["CrossArea_cluster", "CrossArea_subclass", "Class"],
        )
        expanded_schema = expand_schema(
            config=None, yaml_obj=decorated_schema, value_set_names=["CellTypeEnum"]
        )
        self.assertIsNotNone(expanded_schema)

        self.assertTrue(len(expanded_schema["enums"]) >= 3)
        self.assertTrue("CellTypeEnum" in expanded_schema["enums"])
        self.assertTrue(
            len(expanded_schema["enums"]["CellTypeEnum"]["permissible_values"]) > 20
        )


if __name__ == "__main__":
    unittest.main()
