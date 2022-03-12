#* Variables
SHELL := /usr/bin/env bash
PYTHON := python


.PHONY: help
help: ## print this help message.
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


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
