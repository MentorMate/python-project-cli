# MM Python CLI-Pipeline
A CLI tool for generating Django and FastAPI projects.

![Tests](https://github.com/MentorMate/python-project-cli/actions/workflows/tests.yaml/badge.svg)
![Deploy](https://github.com/MentorMate/python-project-cli/actions/workflows/release.yaml/badge.svg)

## Overview
This is a python-cli tool for interactive project setup, following best practices for **Django** and **FastAPI**.
In order to assure easier distribution, the project is deployed as **pypi** package.
For optimal maintenance the project utilizes the **tox** framework.

## Installation
TODO

## Commands
TODO

### Flags
TODO

## Features
TODO

### Frameworks
- Django
- FastAPI

### Testing
TODO

## Package Maintenance
### Development
- Include new members in `CODEOWNERS`

- Prerequisites:

  Install and activate `virtualenv` and install the `requirements_dev.txt`. **Make sure you use python3.11+**
  ```bash
  python -m venv venv
  . venv/bin/activate
  pip install -r requirements_dev.txt
  ```

- pre-commit setup
  Install the `pre-commit` hooks
  ```bash
  pre-commit install
  ```

- git pre-push hook
  Configure a pre-push hook that runs the unit tests before pushing to the repository
  ```bash
  echo -e '#!/bin/sh\n\ntox' >> .git/hooks/pre-push
  chmod ug+x .git/hooks/pre-push
  ```

### Manual package update
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
[LICENSE](https://github.com/MentorMate/python-project-cli/blob/development/LICENSE) file.
