.PHONY: lint test split sync

##########
# Manala #
##########

MANALA_DIR := $(abspath $(patsubst %/make/Makefile,%,$(firstword $(filter %.manala/make/Makefile,$(MAKEFILE_LIST)))))

include \
	$(MANALA_DIR)/make/Makefile.manala \
	$(MANALA_DIR)/make/Makefile.travis \
	$(MANALA_DIR)/make/Makefile.gitsplit

-include \
	$(MANALA_CURRENT_DIR)/.env

MANALA_VERBOSE := $(if $(VERBOSE),$(VERBOSE),$(MANALA_VERBOSE))

#########
# Roles #
#########

ROLES_ALL  := $(sort $(patsubst %/,%,$(wildcard */)))
ROLES_DIFF := $(filter-out .manala,$(sort $(shell git diff --name-only $(TRAVIS_COMMIT_RANGE)| grep "/" | cut -d/ -f1)))

#############
# Partition #
#############

PART ?= 1/1

PARTITION_PART  := $(call list_first,$(call list_split,/,$(PART)))
PARTITION_PARTS := $(call list_last,$(call list_split,/,$(PART)))

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
			$$(MAKE) --silent --directory=$$(ROLE) lint, \
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
			$$(MAKE) --silent --directory=$$(ROLE) test, \
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
	$(call help,split,Split git repositories)

split:
	$(call gitsplit)

########
# Sync #
########

MANALA_HELP += $(SYNC_HELP)

SYNC_HELP = \
	$(call help_section,Sync) \
	$(call help,sync,Sync roles)

sync:
	$(call fail_unless,FROM)
	$(call confirm,Please confirm sync from \"$(FROM)\" ansible role)
	for ROLE in */; do \
		echo $$ROLE; \
		cp $$FROM/.gitignore $$ROLE; \
		cp $$FROM/.travis.yml $$ROLE; \
		cp -r $$FROM/.manala $$ROLE; \
	done
