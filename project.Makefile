## Add your own custom Makefile targets here
SCHEMA_FOLDER = $(SRC)/$(SCHEMA_NAME)/schema
BUILD_FOLDER = build

.PHONY: merged_schemas classes build

merged_schemas:
	cp $(SCHEMA_FOLDER)/cell_annotation_schema.yaml $(BUILD_FOLDER)/general_schema.yaml
	gen-linkml $(SCHEMA_FOLDER)/BICAN/BICAN_schema.yaml --output $(BUILD_FOLDER)/BICAN_schema.yaml --mergeimports --format yaml
	gen-linkml $(SCHEMA_FOLDER)/CAP/CAP_schema.yaml --output $(BUILD_FOLDER)/CAP_schema.yaml --mergeimports --format yaml

classes: merged_schemas
	gen-python $(BUILD_FOLDER)/BICAN_schema.yaml --no-slots > $(PYMODEL)/cell_annotation_schema.py
	gen-python $(BUILD_FOLDER)/BICAN_schema.yaml --no-slots > $(PYMODEL)/bican/cell_annotation_schema.py
	gen-python $(BUILD_FOLDER)/CAP_schema.yaml --no-slots > $(PYMODEL)/cap/cell_annotation_schema.py

build: merged_schemas classes
	echo "Release products generated."

