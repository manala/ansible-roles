.SILENT:

include .manala/Makefile

NAMESPACE = manala
COLLECTION = roles
VERSION = $(shell yq '.version' galaxy.yml)

###########
# Version #
###########

## Version - Get collection version
version: SHELL := $(MANALA_DOCKER_SHELL)
version:
	printf $(VERSION)
.PHONY: version

########
# Lint #
########

## Lint - Lint collection [VERBOSE]
lint: SHELL := $(MANALA_DOCKER_SHELL)
lint:
	ansible-lint \
		$(if $(VERBOSE), -v) \
		--force-color
.PHONY: lint

########
# Test #
########

## Test - Run all collection tests (but doc and coverage)
test: test.sanity test.units test.integration
.PHONY: test

## Test - Run collection sanity tests [VERBOSE]
test.sanity: SHELL := $(MANALA_DOCKER_SHELL)
test.sanity:
	ansible-test sanity \
		--requirements \
		--venv \
		--python 3.11 \
		$(if $(VERBOSE), --verbose) \
		--color yes \
		--exclude .github/ \
		--exclude .manala/
.PHONY: test.sanity

## Test - Run collection units tests [VERBOSE|COVERAGE]
test.units: SHELL := $(MANALA_DOCKER_SHELL)
test.units:
	ansible-test units \
		--requirements \
		--venv \
		--python 3.11 \
		$(if $(VERBOSE), --verbose) \
		$(if $(COVERAGE), --coverage) \
		--color yes
.PHONY: test.units

## Test - Run collection integration tests [VERBOSE|COVERAGE]
test.integration: SHELL := $(MANALA_DOCKER_SHELL)
test.integration:
	ansible-test integration \
		--requirements \
		--venv \
		--python 3.11 \
		$(if $(VERBOSE), --verbose) \
		$(if $(COVERAGE), --coverage) \
		--color yes
.PHONY: test.integration

## Test - Run collection documentation tests [VERBOSE]
test.doc: SHELL := $(MANALA_DOCKER_SHELL)
test.doc:
	$(foreach type,module filter, \
		$(foreach plugin,$(shell ansible-doc --list $(NAMESPACE).$(COLLECTION) --type $(type) --json | jq --raw-output 'keys[]'), \
			ansible-doc \
				$(if $(VERBOSE), --verbose) \
				--type $(type) \
				$(plugin) > /dev/null && \
		) \
	) true
.PHONY: test.doc

## Test - Run collection coverage [VERBOSE]
test.coverage: SHELL := $(MANALA_DOCKER_SHELL)
test.coverage:
	ansible-test coverage xml \
		--requirements \
		--venv \
		--python 3.11 \
		--group-by command \
		--group-by version \
		$(if $(VERBOSE), --verbose) \
		--color yes
.PHONY: test.coverage

############
# Molecule #
############

## Molecule - Run molecule test [SCENARIO]
molecule.test: SHELL := $(MANALA_DOCKER_SHELL)
molecule.test:
	PY_COLORS=1 molecule test \
		$(if $(SCENARIO), --scenario-name $(SCENARIO), --all)
.PHONY: molecule.test

## Molecule - Rune molecule converge [SCENARIO]
molecule.converge: SHELL := $(MANALA_DOCKER_SHELL)
molecule.converge:
	$(call manala_error_if_not, $(SCENARIO), SCENARIO has not been specified)
	PY_COLORS=1 molecule converge \
		--scenario-name $(SCENARIO)
.PHONY: molecule.converge

###################
# Build / Publish #
###################

## Build - Build collection [VERBOSE]
build: SHELL := $(MANALA_DOCKER_SHELL)
build:
	ansible-galaxy collection build \
		--output-path build \
		--force \
		$(if $(VERBOSE), --verbose)
		
.PHONY: build

## Publish - Publish collection [VERBOSE]
publish: SHELL := $(MANALA_DOCKER_SHELL)
publish:
	ansible-galaxy collection publish build/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz \
		$(if $(VERBOSE), --verbose)
.PHONY: publish
