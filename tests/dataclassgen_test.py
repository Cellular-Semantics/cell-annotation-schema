import os
import unittest

from cell_annotation_schema.file_utils import read_schema, get_json_from_file
from cell_annotation_schema.generator.dataclassgen import get_py_instance

from rdflib import Graph

ROOT = os.path.join(os.path.dirname(__file__), "..")
SCHEMA_DIR = os.path.join(ROOT, "build")
DATA_DIR = os.path.join(ROOT, "examples/")
TESTDATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "test_data/rdf/"
)


class DataClassGeneratorTestCase(unittest.TestCase):

    def test_instantiate_class(self):
        json_data = get_json_from_file(os.path.join(TESTDATA, "AIT_MTG_data_short_no_id.json"))
        bican_linkml_schema = read_schema("bican")
        obj = get_py_instance(json_data, "bican", bican_linkml_schema)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.title, "MTG")
        self.assertEqual(1, len(obj.annotations))
        annotation_0 = next(iter(obj.annotations.values()))
        self.assertEqual("VLMC_1", annotation_0.cell_fullname)

    def test_instantiate_class2(self):
        json_data = get_json_from_file(os.path.join(DATA_DIR, "BICAN_schema_specific_examples/Yao_ABC_labelset.json"))
        bican_linkml_schema = read_schema("bican")
        obj = get_py_instance(json_data, "bican", bican_linkml_schema)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.title, "title")
        self.assertEqual(3, len(obj.annotations))
        annotation_0 = next(iter(obj.annotations.values()))
        self.assertEqual("1_MSN", annotation_0.cell_label)
