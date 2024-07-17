"""Data test."""
import os
import glob
import unittest

from cell_annotation_schema.schema_validator import run_validator

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "examples/")
DATA_DIR_BICAN = os.path.join(DATA_DIR, "BICAN_schema_specific_examples/")
DATA_DIR_CAP = os.path.join(DATA_DIR, "CAP_schema_specific_files/")

# SCHEMA_DIR = os.path.join(ROOT, "build")
SCHEMA_DIR = "../../build/"


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        try:
            run_validator(
                path_to_schema_dir=SCHEMA_DIR,
                schema_file="general_schema.yaml",
                path_to_test_dir=DATA_DIR,
            )
            run_validator(
                path_to_schema_dir=SCHEMA_DIR,
                schema_file="BICAN_schema.yaml",
                path_to_test_dir=DATA_DIR_BICAN,
            )
            run_validator(
                path_to_schema_dir=SCHEMA_DIR,
                schema_file="CAP_schema.yaml",
                path_to_test_dir=DATA_DIR_CAP,
            )
        except Exception as e:
            self.fail(f"Validation Failed: {e}")
