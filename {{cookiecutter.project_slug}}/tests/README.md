# Welcome to {{ cookiecutter.project_slug }}'s test suite!

This guide explains how to run the test suite.

## Test requirements

Test requirements are lists under `extras_require` in `setup.py` and can be
installed by running (in the root of this repository):

```shell
pip install .[test]
```

You may use the `-e` parameter.

## Run the tests

The test-suite is a `pytest` one. Use (in the root of this repository):

```shell
pytest tests
```

Or, if your working directory is not the root of this repo:

```shell
pytest /full/or/relative/path/to/tests
```
