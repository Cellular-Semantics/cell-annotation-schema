import unittest
from cell_annotation_schema.file_utils import get_cas_object


class FileUtilsTestCase(unittest.TestCase):

    def test_get_web_url(self):
        taxonomy = get_cas_object("https://github.com/Cellular-Semantics/whole_mouse_brain_taxonomy/raw/refs/heads/main/CCN20230722.json", "bican")
        self.assertEqual("Whole Mouse Brain Taxonomy", taxonomy.title)


if __name__ == '__main__':
    unittest.main()
