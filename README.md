<h1 align="center">📋 copier-fastapi</h1>
<p align="center">
  <i><a href="https://github.com/copier-org/copier">Copier</a> template for <a href="https://github.com/tiangolo/fastapi">fastapi</a> projects.</i>
</p>


<!-- Place https://shields.io/ badges here -->

## Features
- Basic [fastapi](https://github.com/tiangolo/fastapi) setup
- API versioning using [fastapi-versionizer](https://github.com/alexschimpf/fastapi-versionizer)
- Pre-defined HTTP status code error models
- [Poetry](https://github.com/python-poetry/poetry) setup with a pre-defined pyproject.toml
- Continuous integration (CI) pipelines for Github Actions and GitLab CI/CD
- Docker support with build and publish pipelines
- Settings management using [pydantic-settings](https://github.com/pydantic/pydantic-settings)
- [pre-commit](https://github.com/pre-commit/pre-commit) hooks
- [pylint](https://github.com/pylint-dev/pylint) code linter
- [pytest](https://github.com/pytest-dev/pytest/) unit tests
- [VSCode](https://github.com/microsoft/vscode) configuration


## Requirements
First install copier:<br>
([from the official installation documentation](https://copier.readthedocs.io/en/stable/#installation))
```bash
pip install copier
```


## Usage



Make sure the requirements are met, then:
```bash
copier copy --trust "https://github.com/worldworm/copier-fastapi.git" /new/project/path
```

### Update
To update a template after creating a project, run:
```bash
copier update --trust -a .project/.copier-answers.fastapi.yml /some/project/path
```

## Explore more Copier templates
In addition to this template, there are a number of other Copier templates available. For an overview of all available templates, visit the [Templates Showcase repository](https://github.com/worldworm/copier-showcase).

---
<p align="center">
  <i>© <a href="https://github.com/worldworm">worldworm</a> 2023</i><br>
  <i>Licensed under <a href="https://github.com/worldworm/copier-fastapi/blob/main/LICENSE">MIT</a></i><br>
</p>
