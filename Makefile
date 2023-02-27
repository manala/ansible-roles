.SILENT:

-include .manala/Makefile

########
# Lint #
########

## Lint - Lint collection [VERBOSE]
lint:
	$(call manala_docker_shell, ansible-lint \
		$(if $(VERBOSE), -v) \
		--force-color \
	)
.PHONY: lint

########
# Test #
########

## Test - Run all tests (but coverage)
test: test.sanity test.units test.integration
.PHONY: test

## Test - Run sanity tests [VERBOSE]
test.sanity:
	$(call manala_docker_shell, ansible-test sanity \
		--requirements \
		--python 3.9 \
		$(if $(VERBOSE), --verbose) \
		--color \
		--exclude .github/ \
		--exclude .manala/ \
	)
.PHONY: test.sanity

## Test - Run units tests [VERBOSE|COVERAGE]
test.units:
	$(call manala_docker_shell, ansible-test units \
		--requirements \
		--python 3.9 \
		$(if $(VERBOSE), --verbose) \
		$(if $(COVERAGE), --coverage) \
		--color \
	)
.PHONY: test.units

## Test - Run integration tests [VERBOSE|COVERAGE]
test.integration:
	$(call manala_docker_shell, ansible-test integration \
		--requirements \
		--python 3.9 \
		$(if $(VERBOSE), --verbose) \
		$(if $(COVERAGE), --coverage) \
		--color \
	)
.PHONY: test.integration

## Test - Run coverage [VERBOSE]
test.coverage:
	$(call manala_docker_shell, ansible-test coverage xml \
		--requirements \
		--python 3.9 \
		--group-by command \
		--group-by version \
		$(if $(VERBOSE), --verbose) \
		--color \
	)
.PHONY: test.coverage

############
# Molecule #
############

## Molecule - Run molecule test [SCENARIO]
molecule.test:
	$(call manala_docker_shell, PY_COLORS=1 molecule test \
		$(if $(SCENARIO), --scenario-name $(SCENARIO), --all) \
	)
.PHONY: molecule.test

## Molecule - Rune molecule converge [SCENARIO]
molecule.converge:
	$(call manala_error_if_not, $(SCENARIO), SCENARIO has not been specified)
	$(call manala_docker_shell, PY_COLORS=1 molecule converge \
		--scenario-name $(SCENARIO) \
	)
.PHONY: molecule.converge

##############
# Collection #
##############

MANALA_COLLECTION = manala-roles-*.tar.gz

define collection
	$(call manala_docker_shell, ansible-galaxy collection $(1))
endef

## Collection - Build collection
collection.build:
	rm -rf $(MANALA_COLLECTION)
	$(call collection, build --force --verbose)
.PHONY: collection.build

## Collection - Publish collection [COLLECTION_API_TOKEN]
collection.publish:
	$(call manala_error_if_not, $(COLLECTION_API_TOKEN), COLLECTION_API_TOKEN has not been specified)
	$(call collection, publish $(MANALA_COLLECTION) --api-key $(COLLECTION_API_TOKEN))
.PHONY: collection.publish
