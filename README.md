# MM Python CLI-Pipeline
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
A CLI tool for generating Django and FastAPI projects.

## Overview
This is a python-cli tool for interactive project setup, following best practices for **Django** and **FastAPI**, along with CI/CD, linter and testing. In order to assure easier distribution, the project is deployed as **pypi** package.

## Installation
TODO

## Commands
TODO

### Flags
TODO

## Features
TODO

### Framework
- Django
- FastAPI

### Testing
TODO

## Package Maintenance
Prerequisites:

- Install `build` and `twine` on root.
```bash
python3 -m pip install --upgrade build
python -m pip pinstall --upgrade twine
```

- Configure **pypi** token in `~/.pypirc`
```
[testpypi]
  username = __token__
  password = <TOKEN>
```
- Update project version in `pyproject.toml` -> `version`
```toml
...
[project]
name = "python_project_cli"
version = "1.0.0" <--- new version here
...
```

- Build new .whl and .tar.gz
```bash
python3 -m build
```

- Upload new version to pypi **TODO: update testpypi after v1.0.0**
```bash
twine upload --repository testpypi dist/*
```

## License

PYTHON-PROJECT-CLI is MIT licensed, as found in the
[LICENSE](https://github.com/MentorMate/python-project-cli/LICENSE) file.
