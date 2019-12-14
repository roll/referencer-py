# referencer-py

[![Travis](https://img.shields.io/travis/roll/referencer-py/master.svg)](https://travis-ci.org/roll/referencer-py)
[![Coveralls](http://img.shields.io/coveralls/roll/referencer-py.svg?branch=master)](https://coveralls.io/r/roll/referencer-py?branch=master)
[![PyPi](https://img.shields.io/pypi/v/referencer.svg)](https://pypi.python.org/pypi/referencer)
[![Github](https://img.shields.io/badge/github-master-brightgreen)](https://github.com/roll/referencer-py)

Generate a markdown reference from your public API docstrings and add it to your readme.

## Features

- Uses `pydoc-markdown` under the hood

## Installation

The package uses semantic versioning. It means that major versions  could include breaking changes.

```bash
$ pip install referencer
```

## Documentation

```bash
referencer package README.md --in-place
```

## Reference

### `cli`
```python
cli(package, document, **options)
```
Command-line interface

```
Usage: referencer [OPTIONS] PACKAGE DOCUMENT

Options:
  --in-place               [default: False]
  --package-pattern TEXT   [default: from \.(\w+) import (\w+)]
  --document-section TEXT  [default: ## Reference]
  --version                Show the version and exit.
  --help                   Show this message and exit.
```


### `generate_document`
```python
generate_document(package, document, package_pattern='from \\.(\\w+) import (\\w+)', document_section='## Reference')
```
Generate document

### `generate_reference`
```python
generate_reference(package, package_pattern='from \\.(\\w+) import (\\w+)')
```
Generate reference

## Contributing

```python
virtualenv .python -ppython3.7
source .python/bin/activate
make install
make test
```

## Changelog

### v0.1

- Initial version
