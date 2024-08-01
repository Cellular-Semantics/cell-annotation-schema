import os
import unittest

from cell_annotation_schema.ontology.export import dump_to_rdf, populate_ids
from cell_annotation_schema.file_utils import read_schema
from cell_annotation_schema.ontology.schema import decorate_linkml_ontology_schema, expand_schema

from rdflib import Graph

ROOT = os.path.join(os.path.dirname(__file__), "..")
SCHEMA_DIR = os.path.join(ROOT, "build")

TESTDATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "test_data/rdf/"
)
TEST_OUTPUT = os.path.join(TESTDATA, "output_small.rdf")


class LinkMLDataTestCase(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile(TEST_OUTPUT):
            os.remove(TEST_OUTPUT)

    def test_rdf_dump(self):
        data = populate_ids(os.path.join(TESTDATA, "AIT_MTG_data_short.json"), ontology_namespace="MTG",
                            ontology_id="AIT_MTG")

        bican_linkml_schema = read_schema("bican")
        decorated_schema = decorate_linkml_ontology_schema(
            bican_linkml_schema,
            ontology_namespace="MTG",
            ontology_iri="https://purl.brain-bican.org/ontology/AIT_MTG/",
            labelsets=["CrossArea_cluster", "CrossArea_subclass", "Class"],
        )
        decorated_schema = expand_schema(
            config=None, yaml_obj=decorated_schema, value_set_names=["CellTypeEnum"]
        )

        # from ruamel.yaml import YAML
        # yaml = YAML()
        # with open('./test_data/rdf/decorated_schema.yaml', 'wb') as f:
        #     yaml.dump(decorated_schema, f)
        # cli: gen-python decorated_schema.yaml > decorated_schema.py

        rdf_graph = dump_to_rdf(
            schema=decorated_schema,
            instance=data,
            ontology_namespace="MTG",
            ontology_iri="https://purl.brain-bican.org/ontology/AIT_MTG/",
            schema_name="bican",
            labelsets=["CrossArea_cluster", "CrossArea_subclass", "Class"],
            output_path=TEST_OUTPUT,
            validate=False,

        )
        self.assertIsNotNone(rdf_graph)
        # rdf_graph.serialize(destination="rdf_graph.rdf", format="xml")  # TODO:for debugging
        # expected graph (excluding existential restrictions)
        expected_graph = Graph()
        expected_graph.parse(
            os.path.join(TESTDATA, "expected_ouput_1.owl"), format="xml"
        )

        self.assertTrue(len(rdf_graph) > len(expected_graph))
        for stmt in expected_graph:
            self.assertTrue(stmt in rdf_graph)


if __name__ == "__main__":
    unittest.main()
