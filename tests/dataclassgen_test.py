import os
import unittest

from cell_annotation_schema.file_utils import read_schema, get_json_from_file
from cell_annotation_schema.generator.dataclassgen import get_py_instance
from cell_annotation_schema.datamodel.bican.cell_annotation_schema import BicanAnnotation, BicanTaxonomy

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
        annotation_0 = obj.annotations[0]
        self.assertEqual("VLMC_1", annotation_0.cell_fullname)

    def test_instantiate_class2(self):
        json_data = get_json_from_file(os.path.join(DATA_DIR, "BICAN_schema_specific_examples/Yao_ABC_labelset.json"))
        bican_linkml_schema = read_schema("bican")
        obj = get_py_instance(json_data, "bican", bican_linkml_schema)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.title, "title")
        self.assertEqual(3, len(obj.annotations))

        annotation_0 = obj.annotations[0]
        self.assertEqual("1_MSN", annotation_0.cell_label)

    def test_instantiate_class_siletti(self):
        json_data = get_json_from_file(os.path.join(TESTDATA, "Siletti_all_non_neuronal_cells.json"))
        print(len(json_data["annotations"]))
        bican_linkml_schema = read_schema("bican")

        obj = get_py_instance(json_data, "bican", bican_linkml_schema)
        self.assertIsNotNone(obj)
        self.assertEqual(BicanTaxonomy, type(obj))
        self.assertEqual(obj.title, "Cell type annotations for the whole human brain")
        self.assertEqual(89, len(obj.annotations))
        self.assertEqual(BicanAnnotation, type(obj.annotations[0]))

        annotation_0 = obj.annotations[0]
        self.assertEqual("Microglia", annotation_0.cell_label)
        self.assertEqual("supercluster_term", annotation_0.labelset)

        index = 0
        for annotation in obj.annotations:
            if annotation.author_annotation_fields:
                print(annotation.author_annotation_fields)
                # self.assertEqual(dict, type(annotation.author_annotation_fields))
                # self.assertNotEqual(JsonObj, type(annotation.author_annotation_fields))
                self.assertEqual("4", annotation.author_annotation_fields["Cluster ID"])
                annotation.author_annotation_fields = {"Cluster ID": "4"}
                print(annotation.author_annotation_fields)
                print(type(annotation.author_annotation_fields))
                break
            index += 1

    def test_json_obj(self):
        from cell_annotation_schema.datamodel.bican.cell_annotation_schema import Labelset
        taxonomy = BicanTaxonomy("title", "author", annotations=[BicanAnnotation(labelset="labelset",
                                                                                 cell_label="label",
                                                                                 cell_set_accession="accession",
                                                                                 parent_cell_set_accession="parent_cell_set_accession")], labelsets=[Labelset("labelset", "labelset_description")])
        annotation = taxonomy.annotations[0]
        print(annotation.author_annotation_fields)
        annotation.author_annotation_fields = {"Cluster ID": "4"}
        from jsonasobj2 import JsonObj
        self.assertTrue(isinstance(annotation.author_annotation_fields, JsonObj))
        print(annotation.author_annotation_fields._as_dict)
        print(type(annotation.author_annotation_fields))


