"""
Linkml data class generator (gen-python) is generating problematic code because of the subclass and id mechanism we use.

Details of the issue:
Taxonomy-annotations doesn't have a id field so it uses the first slot as id slot (which is labelset).
BicanTaxonomy-annotations (with range Bican Annotations) has a id field so it uses the cell_set_accession field as id slot and works fine.

When we use the gen-python command on the schema, BicanTaxonomy dataclass post_init normalisation code is generated correctly as follows:
```
_normalize_inlined_as_dict(slot_name="annotations", slot_type=BicanAnnotation, key_name="cell_set_accession", keyed=True)
```

But the Taxonomy dataclass post_init normalisation code is generated as follows (expectedly but not correctly):
```
_normalize_inlined_as_dict(slot_name="annotations", slot_type=Annotation, key_name="labelset", keyed=False)
```

And since the BicanTaxonomy post_init is calling the super.post_init, it is trying to normalise the Annotation dataclass
 with the labelset field as id field which is not correct.

Solution this code applies:

We read schema into memory and remove `annotations` slot from the Taxonomy class and add it to BicanTaxonomy
(as if it is not inherited but its own slot) so that the problematic normalisation code is not generated.
"""
import os

from pathlib import Path
from typing import Union
from linkml import generators

from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.loaders import yaml_loader

from cell_annotation_schema.file_utils import read_schema
from cell_annotation_schema.ontology.schema import decorate_linkml_schema

SOURCE_DIR = Path(__file__).parent.parent


def generate_data_class(cas_schema: Union[str, dict], class_path: str):
    """
    Generate data class from CAS schema.

    Args:
        cas_schema: CAS schema path or dict representing it.
        class_path: Output class path.
    Returns:
        str: Data class string.
    """
    schema_def = read_schema(cas_schema)
    schema_dict = decorate_linkml_schema(schema_def)
    schema_def = yaml_loader.load(schema_dict, target_class=SchemaDefinition)
    gen = generators.PythonGenerator(schema_def)
    output = gen.serialize()
    with open(class_path, "w") as class_file:
        class_file.write(output)


if __name__ == "__main__":
    generate_data_class("base", os.path.join(SOURCE_DIR, "datamodel/cell_annotation_schema.py"))
    generate_data_class("bican", os.path.join(SOURCE_DIR, "datamodel/bican/cell_annotation_schema.py"))
    generate_data_class("cap", os.path.join(SOURCE_DIR, "datamodel/cap/cell_annotation_schema.py"))