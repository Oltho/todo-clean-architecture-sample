#* Variables
SHELL := /usr/bin/env bash
PYTHON := python


.PHONY: help
help: ## print this help message.
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


# CI
## test
.PHONY: test
test: ## run test suite.
	pytest
	@echo -e "\n=> pytest done. \n\n"

## code style
.PHONY: flake8
flake8: ## run flake8 check (codestyle).
	flake8
	@echo -e "\n=> flake8 done. \n\n"

.PHONY: isort
isort: ## run isort check (codestyle).
	isort --diff --check-only .
	@echo -e "\n=> isort done. \n\n"

.PHONY: black
black: ## run black check (codestyle).
	black --diff --check --config pyproject.toml .
	@echo -e "\n=> black done. \n\n"

.PHONY: check-codestyle
check-codestyle: flake8 isort black ## run all codestyle check.
	@echo -e "\n=> check-codestyle done. \n\n"

## security
.PHONY: safety
safety: ## run safety check (codestyle).
	safety check --full-report
	@echo -e "\n=> safety done. \n\n"

.PHONY: bandit
bandit: ## run bandit check (codestyle).
	bandit -ll --recursive todo_sample tests
	@echo -e "\n=> bandit done. \n\n"

.PHONY: check-security
check-security: safety bandit ## run all security check.
	@echo -e "\n=> check-security done. \n\n"

## code lint
.PHONY: mypy
mypy: ## run mypy check (codelint).
	mypy --config-file setup.cfg
	@echo -e "\n=> mypy done. \n\n"

.PHONY: ci
ci: test check-codestyle mypy check-security  ## run all CI check (test, codestyle, codelint, security).

# build
.PHONY: build
build: build-remove  ## build python package.
	python -m build .

.PHONE: publish
publish:  ## publish the package to pypi
	python -m twine check dist/*
	python -m twine upload dist/*

# Cleaning
.PHONY: build-remove
build-remove:  ## remove build folder.
	rm -rf build/

.PHONY: dist-remove
dist-remove:  ## remove build folder.
	rm -rf dist/

.PHONY: clean-all
clean-all: build-remove dist-remove ## clean all
