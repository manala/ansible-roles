.PHONY: lint test split sync collection

##########
# Manala #
##########

MANALA_MAKE_DIR := $(abspath $(patsubst %/Makefile,%,$(lastword $(MAKEFILE_LIST))))

include \
	$(MANALA_MAKE_DIR)/Makefile.manala \
	$(MANALA_MAKE_DIR)/Makefile.travis \
	$(MANALA_MAKE_DIR)/Makefile.gitsplit \
	$(MANALA_MAKE_DIR)/Makefile.collection



-include \
	$(MANALA_CURRENT_DIR)/.env

MANALA_VERBOSE := $(if $(VERBOSE),$(VERBOSE),$(MANALA_VERBOSE))

#########
# Roles #
#########

ROLES_ALL  = $(filter-out $(ROLES_DEPRECATED),$(sort $(patsubst roles/%/,%,$(wildcard roles/*/))))
ROLES_DIFF = $(filter-out $(ROLES_DEPRECATED),$(sort $(shell git diff --name-only $(TRAVIS_COMMIT_RANGE)| grep "^roles/" | cut -d/ -f2)))

prout:
	echo $(ROLES_DIFF)

#############
# Partition #
#############

PART ?= 1/1

PARTITION_PART  := $(call list_split_first,/,$(PART))
PARTITION_PARTS := $(call list_split_last,/,$(PART))

########
# Lint #
########

MANALA_HELP += $(LINT_HELP)\n

LINT_HELP = \
	$(call help_section,Lint) \
	$(call help,Lint,     Lint roles)

lint:
	$(call list_loop,ROLE,$(call list_partition,$(PARTITION_PART),$(PARTITION_PARTS),$(if $(ROLES),$(ROLES),$(ROLES_ALL))), \
		$$(call if_in,$$(ROLE),$$(ROLES_ALL), \
			$$(MAKE) --silent --directory=$$(ROLE) molecule.lint, \
			$$(call log_error,Role \"$$(ROLE)\" is not available) ; exit 1 \
		), \
		TRAVIS_FOLD \
	)

LINT_HELP += $(call help,lint.diff,Lint roles - Diff)
lint.diff: ROLES = $(ROLES_DIFF)
lint.diff: lint

########
# Test #
########

MANALA_HELP += $(TEST_HELP)\n

TEST_HELP = \
	$(call help_section,Test) \
	$(call help,test,     Test roles)

test:
	$(call list_loop,ROLE,$(call list_partition,$(PARTITION_PART),$(PARTITION_PARTS),$(if $(ROLES),$(ROLES),$(ROLES_ALL))), \
		$$(call if_in,$$(ROLE),$$(ROLES_ALL), \
			$$(MAKE) --silent --directory=roles/$$(ROLE) molecule.test, \
			$$(call log_error,Role \"$$(ROLE)\" is not available) ; exit 1 \
		) \
	)

TEST_HELP += $(call help,test.diff,Test roles - Diff)
test.diff: ROLES = $(ROLES_DIFF)
test.diff: test

#########
# Split #
#########

MANALA_HELP += $(SPLIT_HELP)\n

SPLIT_HELP = \
	$(call help_section,Split) \
	$(call help,split,Split ansible roles)

split:
	$(call confirm,Please confirm split of *ALL* ansible roles)
	$(call gitsplit)

########
# Sync #
########

MANALA_HELP += $(SYNC_HELP)\n

SYNC_HELP = \
	$(call help_section,Sync) \
	$(call help,sync,Sync roles)

sync:
	$(call fail_if_not,$(FROM),FROM is empty or not set)
	$(call confirm,Please confirm sync from \"$(FROM)\" ansible role)
	for ROLE in roles/*; do \
		echo $$ROLE | cut -d/ -f2; \
		cp roles/$$FROM/.gitignore $$ROLE; \
 		cp roles/$$FROM/.travis.yml $$ROLE; \
 		cp -r roles/$$FROM/.manala $$ROLE; \
	done

sync.molecule:
	$(call fail_if_not,$(FROM),FROM is empty or not set)
	$(call confirm,Please confirm sync from \"$(FROM)\" ansible role)
	for ROLE in roles/*; do \
		echo $$ROLE | cut -d/ -f2; \
		cp roles/$$FROM/molecule/default/molecule.yml $$ROLE/molecule/default/molecule.yml; \
 		cp roles/$$FROM/molecule/.yamllint $$ROLE/molecule; \
 		cp roles/$$FROM/molecule/default/verify.yml $$ROLE/molecule/default/verify.yml; \
	done
SYNC_HELP +=$(call help,sync.molecule,Sync molecule) \

##############
# Collection #
##############

MANALA_COLLECTION = ./manala-roles-*.tar.gz | cut -d/ -f2

MANALA_HELP += $(COLLECTION_HELP)

COLLECTION_HELP = \
	$(call help_section,Collection) \

define collection
	$(call docker_collection, ansible-galaxy collection $(1))
endef

collection.prepare:
	./script.py

COLLECTION_HELP +=$(call help,collection.prepare,Prepare collection) \

collection.build:
	$(call collection,build --force)

COLLECTION_HELP +=$(call help,collection.build,  Create collection) \

collection.publish:
	$(call collection,publish $(MANALA_COLLECTION) --api-key $(COLLECTION_API_TOKEN)

COLLECTION_HELP += $(call help,collection.publish,Publish collection)
