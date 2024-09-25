import os
import unittest

from cell_annotation_schema.file_utils import read_schema, get_json_from_file
from cell_annotation_schema.generator.dataclassgen import get_py_instance
from cell_annotation_schema.datamodel.bican.cell_annotation_schema import BicanTaxonomy
from cell_annotation_schema.taxonomy_utils import asdict

ROOT = os.path.join(os.path.dirname(__file__), "..")
SCHEMA_DIR = os.path.join(ROOT, "build")
DATA_DIR = os.path.join(ROOT, "examples/")
TESTDATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "test_data/rdf/"
)


class TaxonomyUtilsTestCase(unittest.TestCase):

    def test_instantiate_class_siletti(self):
        json_data = get_json_from_file(os.path.join(TESTDATA, "Siletti_all_non_neuronal_cells.json"))
        bican_linkml_schema = read_schema("bican")

        obj = get_py_instance(json_data, "bican", bican_linkml_schema)
        self.assertIsNotNone(obj)
        self.assertEqual(BicanTaxonomy, type(obj))
        self.assertEqual(obj.title, "Cell type annotations for the whole human brain")

        taxon_dict = asdict(obj)
        self.assertEqual(dict, type(taxon_dict))
        self.assertEqual(taxon_dict["title"], "Cell type annotations for the whole human brain")
        self.assertEqual(89, len(taxon_dict["annotations"]))

        # null value stripped
        self.assertTrue("cellannotation_timestamp" not in taxon_dict)

        annotation_0 = taxon_dict["annotations"][0]
        self.assertEqual("Microglia", annotation_0["cell_label"])
        self.assertEqual("supercluster_term", annotation_0["labelset"])
        # CellTypeEnum unpacked
        self.assertEqual("CL:0000129", annotation_0["cell_ontology_term_id"])
        print(annotation_0["rationale"])

