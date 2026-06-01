.phony : tests, bootstrap, update, console, build, documentation, printversion, release, local_specs, client, versions, surface-diff, remote-version

VERSION := $(shell git describe --tags)
ifeq ($(VERSION),)
    VERSION := v0.0.1
endif

bootstrap:
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip build
	python -m pip install -r requirements.txt
	python -m pip install -r test-requirements.txt
	pip install -e .
console:
tests:
	pytest -m "not integration"
test-integration:
	pytest
	# Run example.py to test integration with Floriday API
	python example.py
build:
	python -m build
quality: tests
	# only run tests for now
documentation:
printversion:
	@python -m setuptools_scm
release:
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "There are uncommitted changes or untracked files"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then \
		echo "Not on main branch"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse HEAD)" != "$$(git rev-parse origin/main)" ]; then \
		echo "Local branch is ahead of origin"; \
		exit 1; \
	fi
	@git tag v$$(python -m setuptools_scm --strip-dev)
	@git tag -f floriday_api_v$(api_version)
	@git push origin v$$(python -m setuptools_scm --strip-dev)
	@git push origin floriday_api_v$(api_version) --force

api_version := 2026v1
url := https://api.staging.floriday.io/suppliers-api-$(api_version)/swagger/UUID/swagger.json
target_dir := .
spec_file := ./specs/floriday-suppliers-api-$(api_version)-swagger-UUID.json

local_specs:
	mkdir -p ./specs
	curl $(url) > $(spec_file)

# Read-only release diagnostics (safe to run any time).
# versions       - print the API version in every source and flag disagreements
# surface-diff   - report public-surface changes BASE..working tree (default BASE=HEAD,
#                  includes untracked files; run after `make client`, before committing)
# remote-version - probe staging for a candidate version (default V=$(api_version))
BASE ?= HEAD
V ?= $(api_version)
versions:
	@python3 scripts/show_versions.py
surface-diff:
	@python3 scripts/surface_diff.py $(BASE)
remote-version:
	@curl -sI -o /dev/null -w "suppliers-api-$(V): HTTP %{http_code}\n" \
		https://api.staging.floriday.io/suppliers-api-$(V)/swagger/index.html

floriday_supplier_client/api_client.py: $(spec_file)
	swagger-codegen generate -i $(spec_file) -l python -o $(target_dir) -DpackageName=floriday_supplier_client
	rm -f git_push.sh .travis.yml -f tox.ini

client: floriday_supplier_client/api_client.py
