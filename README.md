# cell-annotation-schema

General, open-standard schema for cell annotations

## Website

[https://Cellular-Semantics.github.io/cell-annotation-schema](https://Cellular-Semantics.github.io/cell-annotation-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [cell_annotation_schema](src/cell_annotation_schema)
    * [schema](src/cell_annotation_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/cell_annotation_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
