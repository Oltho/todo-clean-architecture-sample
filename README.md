# Todo Clean Architecture Sample package

This is a simple todo application packaged for pypi.

## Requirements

```bash
pip install todo-clean-architecture-sample
```

## Usage

TBD


## Development

### Requirements

- python >= 3.7
- tox

```
git clone https://github.com/Oltho/todo-clean-architecture-sample.git
cd todo-clean-architecture-sample
```

### Pre-commit check
[pre-commit](https://pre-commit.com/) is a framework for managing pre-commit hooks. These hooks help to identify simple issues before committing code for review.

To use this tool, first install it and then the git hooks:

```
$ pip install pre-commit
$ pre-commit install
```

### Testing

#### Tox:
All testing can be done thought `tox`, you can provide the tox environement to run with `tox -e <environement_to_run>`

List of environments availables:

- `flake8`: run flake8 linter
- `isort`: run isort linter
- `black`: run black code formating
- `mypy`: run mypy type checker
- `linters`: run `flake8, isort, black, mypy` tox environments
- `bandit`: run bandit AST
- `safety`: run safety dependencies check
- `security`: run `bandit, safety` tox environments

You can also just run the `tox` command that will run `linters, security` environments.

#### Local:
If you can to run test locally without tox.

Install the package locally with its extras `pip install -e ".[all]"`

You can then use the same command as defined in `tox.ini` under `commands` section of each environments.

These same command are in the `Makefile` and can be use with `make`, but we recommand to run it through `tox` to ensure clean and isolated python enviroment.

You might need to update your `PYTHONPATH` so your tests can detect code in `src`: `export PYTHONPATH=<path_to_the_project>/src`


# Todo

- Integration of SonarQube
- Update code with clean architecture and 12 app factor
- Handle semver
- Automated github release
- CI:
    - github action
    - jenkins


# Acknowledgements

Inspired by:

- [python-package-template](https://github.com/TezRomacH/python-package-template)
- [pyscaffold](https://github.com/pyscaffold/pyscaffold)
- [flask](https://github.com/pallets/flask)
- [django](https://github.com/django/django)
