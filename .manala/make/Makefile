.PHONY: lint test split sync

##########
# Manala #
##########

MANALA_MAKE_DIR := $(abspath $(patsubst %/Makefile,%,$(lastword $(MAKEFILE_LIST))))

include \
	$(MANALA_MAKE_DIR)/Makefile.manala \
	$(MANALA_MAKE_DIR)/Makefile.travis \
	$(MANALA_MAKE_DIR)/Makefile.gitsplit

-include \
	$(MANALA_CURRENT_DIR)/.env

MANALA_VERBOSE := $(if $(VERBOSE),$(VERBOSE),$(MANALA_VERBOSE))

#########
# Roles #
#########

ROLES_ALL  = $(filter-out $(ROLES_DEPRECATED),$(sort $(patsubst %/,%,$(wildcard */))))
ROLES_DIFF = $(filter-out $(ROLES_DEPRECATED) .manala,$(sort $(shell git diff --name-only $(TRAVIS_COMMIT_RANGE)| grep "/" | cut -d/ -f1)))

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
	$(call help,split,Split ansible roles)

split:
	$(call confirm,Please confirm split of *ALL* ansible roles)
	$(call gitsplit)

########
# Sync #
########
MANALA_HELP += $(SYNC_HELP)

SYNC_HELP = \
	$(call help_section,Sync) \
	$(call help,sync,Sync roles)

sync:
	$(call fail_if_not,$(FROM),FROM is empty or not set)
	$(call confirm,Please confirm sync from \"$(FROM)\" ansible role)
	for ROLE in */; do \
		echo $$ROLE; \
		cp $$FROM/.gitignore $$ROLE; \
		cp $$FROM/.travis.yml $$ROLE; \
		cp -r $$FROM/.manala $$ROLE; \
	done
