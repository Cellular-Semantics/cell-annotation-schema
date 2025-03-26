import os
import unittest

from rdflib import URIRef, Graph

from cell_annotation_schema.ontology.export import export_to_rdf


CAS_NS = "https://purl.brain-bican.org/taxonomy/"
OBO_NS = "http://purl.obolibrary.org/obo/"

# ontology resources
dataset_type = URIRef(CAS_NS + "Taxonomy")
annotation_type = URIRef("http://purl.obolibrary.org/obo/PCL_0010001")
labelset_type = URIRef(CAS_NS + "Labelset")
rdftype = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
matrix_file_id = URIRef(CAS_NS + "matrix_file_id")
transferred_cell_label = URIRef(CAS_NS + "transferred_cell_label")
source_taxonomy = URIRef(CAS_NS + "source_taxonomy")
source_node_accession = URIRef(CAS_NS + "source_node_accession")
IAO_0000115 = URIRef(OBO_NS + "IAO_0000115")

TESTDATA = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./test_data/rdf/")
TEST_OUTPUT = os.path.join(TESTDATA, "output.rdf")
TEST_OUTPUT2 = os.path.join(TESTDATA, "CS202210140_non_neuronal.rdf")


class ExportToRDFTestCase(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile(TEST_OUTPUT):
            os.remove(TEST_OUTPUT)
        if os.path.isfile(TEST_OUTPUT2):
            os.remove(TEST_OUTPUT2)

    def test_export_to_rdf(self):
        ontology_namespace = "MTG"
        ontology_iri = "https://purl.brain-bican.org/ontology/AIT_MTG/"

        rdf_graph = export_to_rdf(
            cas_schema="bican",
            data=os.path.join(TESTDATA, "AIT_MTG.json"),
            ontology_namespace=ontology_namespace,
            ontology_iri=ontology_iri,
            output_path=TEST_OUTPUT,
            validate=True,
            include_cells=False,
        )
        self.assertTrue(os.path.isfile(TEST_OUTPUT))

        self.assertEqual(1, len(list(rdf_graph.triples((None, rdftype, dataset_type)))))
        self.assertEqual(
            3, len(list(rdf_graph.triples((None, rdftype, labelset_type))))
        )
        self.assertEqual(
            160, len(list(rdf_graph.triples((None, rdftype, annotation_type))))
        )

        L5_IT_2 = URIRef(ontology_iri + "CrossArea_cluster#4a4d733723")
        triples = list(rdf_graph.triples((L5_IT_2, None, None)))
        self.assertEqual(5, len(triples))
        for triple in triples:
            if str(triple[1]) == CAS_NS + "has_labelset":
                self.assertEqual(ontology_iri + "CrossArea_cluster", str(triple[2]))
            elif str(triple[1]) == "http://www.w3.org/2000/01/rdf-schema#label":
                self.assertEqual("L5 IT_2", str(triple[2]))
            elif str(triple[1]) == "http://purl.obolibrary.org/obo/RO_0015003":
                self.assertEqual(
                    ontology_iri + "CrossArea_subclass#c6694cb883", str(triple[2])
                )
            elif str(triple[1]) == "http://www.w3.org/2004/02/skos/core#preflabel":
                self.assertEqual("L5 IT_2", str(triple[2]))
            elif triple[1] == rdftype:
                self.assertEqual(
                    "http://purl.obolibrary.org/obo/PCL_0010001", str(triple[2])
                )
            else:
                self.fail("Unexpected triple: " + str(triple))

    def test_export_to_rdf_siletti(self):
        ontology_namespace = "CS202210140"
        ontology_iri = "https://purl.brain-bican.org/ontology/CS202210140/"

        rdf_graph = export_to_rdf(
            cas_schema="bican",
            # cas_schema="https://raw.githubusercontent.com/Cellular-Semantics/cell-annotation-schema/main/build/BICAN_schema.yaml",
            # data=os.path.join(TESTDATA, "CS202210140.json"),
            data=os.path.join(TESTDATA, "Siletti_all_non_neuronal_cells.json"),
            ontology_namespace=ontology_namespace,
            ontology_iri=ontology_iri,
            output_path=TEST_OUTPUT2,
            validate=True,
            include_cells=False,
        )

        self.assertTrue(os.path.isfile(TEST_OUTPUT2))
        self.assertEqual(1, len(list(rdf_graph.triples((None, rdftype, dataset_type)))))
        self.assertEqual(
            2, len(list(rdf_graph.triples((None, rdftype, labelset_type))))
        )
        self.assertEqual(
            89, len(list(rdf_graph.triples((None, rdftype, annotation_type))))
        )

        Epen_69 = URIRef(ontology_iri + "CS202210140_70")
        triples = list(rdf_graph.triples((Epen_69, None, None)))
        self.assertEqual(5, len(triples))
        for triple in triples:
            if str(triple[1]) == CAS_NS + "has_labelset":
                self.assertEqual(ontology_iri + "Cluster", str(triple[2]))
            elif str(triple[1]) == "http://www.w3.org/2000/01/rdf-schema#label":
                self.assertEqual("Epen_69", str(triple[2]))
            elif str(triple[1]) == "http://purl.obolibrary.org/obo/RO_0015003":
                self.assertEqual(ontology_iri + "CS202210140_471", str(triple[2]))
            elif str(triple[1]) == CAS_NS + "author_annotation_fields":
                self.assertEqual('{"Cluster ID": "69"}', str(triple[2]))
            elif triple[1] == rdftype:
                self.assertEqual(
                    "http://purl.obolibrary.org/obo/PCL_0010001", str(triple[2])
                )
            else:
                self.fail("Unexpected triple: " + str(triple))

    def test_export_to_rdf_siletti_v2(self):
        ontology_namespace = "CS202210140"
        ontology_iri = "https://purl.brain-bican.org/ontology/CS202210140/"

        rdf_graph = export_to_rdf(
            cas_schema="bican",
            data=os.path.join(
                TESTDATA, "Siletti_all_non_neuronal_cells2.json"
            ),  # with annotation transfer
            ontology_namespace=ontology_namespace,
            ontology_iri=ontology_iri,
            output_path=TEST_OUTPUT2,
            validate=True,
            include_cells=False,
        )

        self.assertTrue(os.path.isfile(TEST_OUTPUT2))
        self.assertEqual(1, len(list(rdf_graph.triples((None, rdftype, dataset_type)))))
        self.assertEqual(
            3, len(list(rdf_graph.triples((None, rdftype, labelset_type))))
        )
        self.assertEqual(
            386, len(list(rdf_graph.triples((None, rdftype, annotation_type))))
        )

        self.assertEqual(
            "https://cellxgene.cziscience.com/e/b165f033-9dec-468a-9248-802fc6902a74.cxg/",
            str(list(rdf_graph.triples((None, matrix_file_id, None)))[0][2]),
        )

        Epen_69 = URIRef(ontology_iri + "CS202210140_70")
        triples = list(rdf_graph.triples((Epen_69, None, None)))
        self.assertEqual(5, len(triples))
        for triple in triples:
            if str(triple[1]) == CAS_NS + "has_labelset":
                self.assertEqual(ontology_iri + "Cluster", str(triple[2]))
            elif str(triple[1]) == "http://www.w3.org/2000/01/rdf-schema#label":
                self.assertEqual("Epen_69", str(triple[2]))
            elif str(triple[1]) == "http://purl.obolibrary.org/obo/RO_0015003":
                self.assertEqual(ontology_iri + "CS202210140_471", str(triple[2]))
            elif str(triple[1]) == CAS_NS + "author_annotation_fields":
                self.assertEqual(
                    '{"Cluster ID": "69", "Class auto_annotation": "EPEN", "Neurotransmitter auto_annotation": "None", "Neuropeptide auto_annotation": "AGT NAMPT NTS NUCB UBL proSAAS", "Subtype auto_annotation": "None", "Transferred MTG Label": "None", "Top three regions": "Hippocampus: 69.2%, Basal forebrain: 11.2%, Amygdala: 7.6%", "Top three dissections": "Human CA1: 17.4%, Human CA1U-CA2U-CA3U: 16.7%, Human CA4C-DGC: 11.0%", "Top Enriched Genes": "DTHD1, CFAP157, RASSF9, ADGB, FAM183A, C11orf88, AC013470.2, AC020718.1, FOXJ1, AC093689.1", "Number of cells": "724.0", "DoubletFinder score": "0.022703475", "Total UMI": "7073.150552", "Fraction unspliced": "0.580179333", "Fraction mitochondrial": "0.020167044", "H19.30.002": "190.0", "H19.30.001": "211.0", "H18.30.002": "323.0", "H18.30.001": "0.0", "Fraction cells from top donor": "0.446132597", "Number of donors": "3.0", "subcluster_id": "None"}',
                    str(triple[2]),
                )
            elif triple[1] == rdftype:
                self.assertEqual(
                    "http://purl.obolibrary.org/obo/PCL_0010001", str(triple[2])
                )
            else:
                self.fail("Unexpected triple: " + str(triple))

        VendAC_14 = URIRef(ontology_iri + "CS202210140_15")
        triples = list(rdf_graph.triples((VendAC_14, None, None)))
        self.assertEqual(6, len(triples))
        has_annotation_transfer = False
        for triple in triples:
            if str(triple[1]) == CAS_NS + "has_labelset":
                self.assertEqual(ontology_iri + "Cluster", str(triple[2]))
            elif str(triple[1]) == "http://www.w3.org/2000/01/rdf-schema#label":
                self.assertEqual("VendAC_14", str(triple[2]))
            elif str(triple[1]) == CAS_NS + "transferred_annotations":
                has_annotation_transfer = True
                at_blanknode = triple[2]
                at_triples = list(rdf_graph.triples((at_blanknode, None, None)))
                self.assertEqual(5, len(at_triples))
                self.assertEqual(
                    "https://purl.brain-bican.org/taxonomy/AnnotationTransfer",
                    str(list(rdf_graph.triples((at_blanknode, rdftype, None)))[0][2]),
                )
                self.assertEqual(
                    "Endo",
                    str(
                        list(
                            rdf_graph.triples(
                                (at_blanknode, transferred_cell_label, None)
                            )
                        )[0][2]
                    ),
                )
                self.assertEqual(
                    "https://purl.brain-bican.org/taxonomy/AIT_MTG/AIT_MTG.json",
                    str(
                        list(rdf_graph.triples((at_blanknode, source_taxonomy, None)))[
                            0
                        ][2]
                    ),
                )
                self.assertEqual(
                    "CrossArea_subclass:48e48631ba",
                    str(
                        list(
                            rdf_graph.triples(
                                (at_blanknode, source_node_accession, None)
                            )
                        )[0][2]
                    ),
                )
                self.assertTrue(
                    "https://purl.brain-bican.org/taxonomy/AIT_MTG/AIT_MTG.json",
                    str(
                        list(rdf_graph.triples((at_blanknode, IAO_0000115, None)))[0][2]
                    ).startswith(
                        "We performed PCA (50 components) on our full dataset, trained"
                    ),
                )
        self.assertTrue(has_annotation_transfer)

    def test_export_to_wmb(self):
        ontology_namespace = "CCN20230722"
        ontology_iri = "https://purl.brain-bican.org/taxonomy/CCN20230722/"
        out_file = os.path.join(TESTDATA, "CCN20230722.rdf")
        # out_file = TEST_OUTPUT

        rdf_graph = export_to_rdf(
            cas_schema="bican",
            data=os.path.join(
                TESTDATA, "CCN20230722.json"
            ),  # with annotation transfer
            ontology_namespace=ontology_namespace,
            ontology_iri=ontology_iri,
            output_path=out_file,
            validate=True,
            include_cells=False,
        )
        self.assertTrue(os.path.isfile(out_file))
        self.assertEqual(1, len(list(rdf_graph.triples((None, rdftype, dataset_type)))))
        self.assertEqual(
            5, len(list(rdf_graph.triples((None, rdftype, labelset_type))))
        )

if __name__ == "__main__":
    unittest.main()
