.phony : tests, bootstrap, update, console, build, documentation, printversion, release

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
	nosetests
build:
	python -m build
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
	@git push origin --tags

api_version := 2024v1
url := https://api.staging.floriday.io/suppliers-api-$(api_version)/swagger/UUID/swagger.json
target_dir := .

api_client:
	swagger-codegen generate -i $(url) -l python -o $(target_dir) -DpackageName=floriday_supplier_client
	rm -f git_push.sh
	rm -f .travis.yml
	rm -f tox.ini
