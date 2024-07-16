## Migrate from json schema to LinkML schema

```
schemauto import-json-schema src/cell_annotation_schema/legacy/general_schema.json -o src/cell_annotation_schema/schema/cell_annotation_schema_v.yaml -n cell-annotation-schema 
```

## Value sets expansion
`CellTypeEnum` expansion

https://github.com/INCATools/ontology-access-kit/blob/main/src/oaklib/utilities/subsets/value_set_expander.py

## Merge schemas

```
make merged_schemas
```

## Generate Python data model

```
make classes
```