## Add your own custom Makefile targets here
#
# make build : generates dataclasses and merged & expanded schemas
# make gendoc : generates documentation
# make gen-project : generates project folder contents

SCHEMA_FOLDER = $(SRC)/$(SCHEMA_NAME)/schema
BUILD_FOLDER = build

DOCDIR_BICAN = $(DOCDIR)/bican
DOCDIR_CAP = $(DOCDIR)/cap

SCHEMA_EXPANDER := $(SRC)/$(SCHEMA_NAME)/schema_expander.py

.PHONY: expanded_schemas merged_schemas classes build

merged_schemas:
	cp $(SCHEMA_FOLDER)/cell_annotation_schema.yaml $(BUILD_FOLDER)/general_schema.yaml
	$(RUN) gen-linkml $(SCHEMA_FOLDER)/BICAN/BICAN_schema.yaml --output $(BUILD_FOLDER)/BICAN_schema.yaml --mergeimports --format yaml --no-materialize-attributes
	$(RUN) gen-linkml $(SCHEMA_FOLDER)/CAP/CAP_schema.yaml --output $(BUILD_FOLDER)/CAP_schema.yaml --mergeimports --format yaml --no-materialize-attributes

expanded_schemas: merged_schemas
	$(RUN) python $(SCHEMA_EXPANDER) expand -i $(BUILD_FOLDER)/general_schema.yaml -o $(BUILD_FOLDER)/general_schema.yaml
	$(RUN) python $(SCHEMA_EXPANDER) expand -i $(BUILD_FOLDER)/BICAN_schema.yaml -o $(BUILD_FOLDER)/BICAN_schema.yaml
	$(RUN) python $(SCHEMA_EXPANDER) expand -i $(BUILD_FOLDER)/CAP_schema.yaml -o $(BUILD_FOLDER)/CAP_schema.yaml

classes: expanded_schemas
#	gen-python $(BUILD_FOLDER)/general_schema.yaml --no-slots > $(PYMODEL)/cell_annotation_schema.py
#	gen-python $(BUILD_FOLDER)/BICAN_schema.yaml --no-slots > $(PYMODEL)/bican/cell_annotation_schema.py
#	gen-python $(BUILD_FOLDER)/CAP_schema.yaml --no-slots > $(PYMODEL)/cap/cell_annotation_schema.py
	$(RUN) python src/cell_annotation_schema/generator/dataclassgen.py

build: expanded_schemas classes
	echo "Release products generated."

# mkdocs generation
$(DOCDIR_BICAN):
	mkdir -p $@

$(DOCDIR_CAP):
	mkdir -p $@

gendoc: $(DOCDIR) $(DOCDIR_BICAN) $(DOCDIR_CAP)
	cp -rf $(SRC)/docs/* $(DOCDIR) ; \
	$(RUN) gen-doc ${GEN_DOC_ARGS} -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-doc ${GEN_DOC_ARGS} -d $(DOCDIR_BICAN) $(BUILD_FOLDER)/BICAN_schema.yaml
	$(RUN) gen-doc ${GEN_DOC_ARGS} -d $(DOCDIR_CAP) $(BUILD_FOLDER)/CAP_schema.yaml

gen-project: build
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST) $(BUILD_FOLDER)/general_schema.yaml --exclude python
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST) $(BUILD_FOLDER)/BICAN_schema.yaml --exclude python
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST) $(BUILD_FOLDER)/CAP_schema.yaml --exclude python

compile-sheets:
	echo "Skipped compiling sheets."

