## Add your own custom Makefile targets here
SCHEMA_FOLDER = $(SRC)/$(SCHEMA_NAME)/schema
BUILD_FOLDER = build

DOCDIR_BICAN = $(DOCDIR)/bican
DOCDIR_CAP = $(DOCDIR)/cap

.PHONY: merged_schemas classes build

merged_schemas:
	cp $(SCHEMA_FOLDER)/cell_annotation_schema.yaml $(BUILD_FOLDER)/general_schema.yaml
	gen-linkml $(SCHEMA_FOLDER)/BICAN/BICAN_schema.yaml --output $(BUILD_FOLDER)/BICAN_schema.yaml --mergeimports --format yaml
	gen-linkml $(SCHEMA_FOLDER)/CAP/CAP_schema.yaml --output $(BUILD_FOLDER)/CAP_schema.yaml --mergeimports --format yaml

classes: merged_schemas
	gen-python $(BUILD_FOLDER)/general_schema.yaml --no-slots > $(PYMODEL)/cell_annotation_schema.py
	gen-python $(BUILD_FOLDER)/BICAN_schema.yaml --no-slots > $(PYMODEL)/bican/cell_annotation_schema.py
	gen-python $(BUILD_FOLDER)/CAP_schema.yaml --no-slots > $(PYMODEL)/cap/cell_annotation_schema.py

build: merged_schemas classes
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

