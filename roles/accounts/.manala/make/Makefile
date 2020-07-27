.PHONY: sh update lint test

##########
# Manala #
##########

MANALA_MAKE_DIR := $(abspath $(patsubst %/Makefile,%,$(lastword $(MAKEFILE_LIST))))

include \
	$(MANALA_MAKE_DIR)/Makefile.manala \
	$(MANALA_MAKE_DIR)/Makefile.docker \
	$(MANALA_MAKE_DIR)/Makefile.host \
	$(MANALA_MAKE_DIR)/Makefile.travis

-include \
	$(MANALA_CURRENT_DIR)/../.env \
	$(MANALA_CURRENT_DIR)/.env

MANALA_VERBOSE := $(if $(VERBOSE),$(VERBOSE),$(MANALA_VERBOSE))

########
# Role #
########

ROLE_DIR       := $(MANALA_CURRENT_DIR)
ROLE_TESTS_DIR := $(ROLE_DIR)/tests

################
# Distribution #
################

DISTRIBUTION_ID      = $(call list_split_first,.,$(DISTRIBUTION))
DISTRIBUTION_RELEASE = $(call list_split_last,.,$(DISTRIBUTION))

##########
# Docker #
##########

MANALA_DOCKER_IMAGE       = manala/test-ansible
MANALA_DOCKER_IMAGE_TAG   = $(if $(ANSIBLE_VERSION),$(ANSIBLE_VERSION)-)$(DISTRIBUTION)
MANALA_DOCKER_MOUNT_DIR   = $(if $(ROLE_MOUNT_DIR),$(ROLE_MOUNT_DIR),/srv/role)
MANALA_DOCKER_HOST        = $(ROLE).$(DISTRIBUTION).test
MANALA_DOCKER_RUN_OPTIONS = --privileged
MANALA_DOCKER_VOLUMES     = \
	$(ROLE_DIR):/etc/ansible/roles/$(ROLE) \
	$(if $(CACHE_DIR), \
		$(call if_in,$(DISTRIBUTION_ID),debian, \
			$(CACHE_DIR)/$(DISTRIBUTION_ID)/$(DISTRIBUTION_RELEASE)/apt/archives:/var/cache/apt/archives \
			$(CACHE_DIR)/$(DISTRIBUTION_ID)/$(DISTRIBUTION_RELEASE)/apt/lists:/var/lib/apt/lists \
		) \
	)
MANALA_DOCKER_ENV         = \
	USER_ID=$(MANALA_USER_ID) \
	GROUP_ID=$(MANALA_GROUP_ID) \
	MANALA_HOST=test \
	MANALA_VERBOSE=$(MANALA_VERBOSE) \
	DISTRIBUTION=$(DISTRIBUTION) \
	DISTRIBUTION_ID=$(DISTRIBUTION_ID) \
	DISTRIBUTION_RELEASE=$(DISTRIBUTION_RELEASE) \
	ANSIBLE_BECOME_FLAGS="$(call escape_spaces,-H -S -n -E)" \
	ANSIBLE_RETRY_FILES_ENABLED=0 \
	ANSIBLE_FORCE_COLOR=1

######
# Sh #
######

MANALA_HELP += $(call if_host,local,$(SH_HELP)\n)

SH_HELP = \
	$(call help_section,Test host shell)

sh: .fail_if_host_not(local)
	$(call fail_if_not,$(DISTRIBUTION),DISTRIBUTION is empty or not set)
	$(call if_in,$(DISTRIBUTION),$(ROLE_DISTRIBUTIONS), \
		$(call docker_shell), \
		$(call log_warning,Shell on \"$(DISTRIBUTION)\" is not supported) \
	)

SH_HELP += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,sh.debian.jessie, Open shell on test host - Debian Jessie))
sh.debian.jessie: DISTRIBUTION = debian.jessie
sh.debian.jessie: sh

SH_HELP += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,sh.debian.stretch,Open shell on test host - Debian Stretch))
sh.debian.stretch: DISTRIBUTION = debian.stretch
sh.debian.stretch: sh

SH_HELP += $(call if_in,debian.buster,$(ROLE_DISTRIBUTIONS),$(call help,sh.debian.buster, Open shell on test host - Debian Buster))
sh.debian.buster: DISTRIBUTION = debian.buster
sh.debian.buster: sh

##########
# Update #
##########

MANALA_HELP += $(call if_host,local,$(UPDATE_HELP)\n)

UPDATE_HELP = \
	$(call help_section,Test host update) \
	$(call help,update,               Update test hosts across distributions)

update: .fail_if_host_not(local)
	$(call list_loop,DISTRIBUTION,$(if $(DISTRIBUTIONS),$(DISTRIBUTIONS),$(ROLE_DISTRIBUTIONS)), \
		$$(call if_in,$$(DISTRIBUTION),$$(ROLE_DISTRIBUTIONS), \
			$$(call log,Update \"$$(DISTRIBUTION)\") ; \
				$$(call docker_pull), \
			$$(call log_warning,Update \"$$(DISTRIBUTION)\" is not supported) \
		) \
	)

UPDATE_HELP += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,update.debian.jessie, Update test host - Debian Jessie))
update.debian.jessie: DISTRIBUTIONS = debian.jessie
update.debian.jessie: update

UPDATE_HELP += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,update.debian.stretch,Update test host - Debian Stretch))
update.debian.stretch: DISTRIBUTIONS = debian.stretch
update.debian.stretch: update

UPDATE_HELP += $(call if_in,debian.buster,$(ROLE_DISTRIBUTIONS),$(call help,update.debian.buster, Update test host - Debian Buster))
update.debian.buster: DISTRIBUTIONS = debian.buster
update.debian.buster: update

########
# Lint #
########

MANALA_HELP += $(call if_host,local,$(LINT_HELP_LOCAL)\n,$(LINT_HELP_TEST)\n)

LINT_HELP       = $(call help_section,Lint)
LINT_HELP_LOCAL = $(LINT_HELP) \
	$(call help,lint,               Lint role across distributions)
LINT_HELP_TEST  = $(LINT_HELP) \
	$(call help,lint,Lint role)

lint: .host_switch(lint)

lint@local: .fail_if_host_not(local)
	$(call list_loop,DISTRIBUTION,$(if $(DISTRIBUTIONS),$(DISTRIBUTIONS),$(ROLE_DISTRIBUTIONS)), \
		$$(call if_in,$$(DISTRIBUTION),$$(ROLE_DISTRIBUTIONS), \
			$$(call log,Lint \"$$(ROLE)\" on \"$$(DISTRIBUTION)\") ; \
				$$(call docker_make,lint@test), \
			$$(call log_warning,Lint \"$$(ROLE)\" on \"$$(DISTRIBUTION)\" is not supported) \
		) \
	)

lint@test: .fail_if_host_not(test)
	ansible-lint --force-color -v $(ROLE_DIR)

LINT_HELP_LOCAL += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,lint.debian.jessie, Lint role - Debian Jessie))
lint.debian.jessie: DISTRIBUTIONS = debian.jessie
lint.debian.jessie: lint@local

LINT_HELP_LOCAL += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,lint.debian.stretch,Lint role - Debian Stretch))
lint.debian.stretch: DISTRIBUTIONS = debian.stretch
lint.debian.stretch: lint@local

LINT_HELP_LOCAL += $(call if_in,debian.buster,$(ROLE_DISTRIBUTIONS),$(call help,lint.debian.buster, Lint role - Debian Buster))
lint.debian.buster: DISTRIBUTIONS = debian.buster
lint.debian.buster: lint@local

########
# Test #
########

TESTS = $(sort \
	$(foreach \
		TEST, \
		$(wildcard $(ROLE_TESTS_DIR)/*.yml), \
		$(if $(findstring .goss.,$(TEST)),, \
			$(patsubst /%,%,$(subst $(ROLE_DIR),,$(TEST))) \
		) \
	) \
)

tests/%.yml: FORCE
	$(call verbose, ,ANSIBLE_STDOUT_CALLBACK=actionable,ANSIBLE_STDOUT_CALLBACK=debug) \
		ansible-playbook $@ \
			--extra-vars="test=$(subst .yml,,$(subst tests/,,$@))" \
			$(if $(TAGS),--tags=$(TAGS))
FORCE:

MANALA_HELP += $(call if_host,local,$(TEST_HELP_LOCAL),$(TEST_HELP_TEST))

TEST_HELP       = $(call help_section,Test)
TEST_HELP_LOCAL = $(TEST_HELP) \
	$(call help,test,               Test role across distributions)
TEST_HELP_BUILD = $(TEST_HELP) \
	$(call help,test,Test role)

test: .host_switch(test)

test@local: .fail_if_host_not(local)
	$(call list_loop,DISTRIBUTION,$(if $(DISTRIBUTIONS),$(DISTRIBUTIONS),$(ROLE_DISTRIBUTIONS)), \
		$$(call if_in,$$(DISTRIBUTION),$$(ROLE_DISTRIBUTIONS), \
		  $$(call log,Test \"$$(ROLE)\" on \"$$(DISTRIBUTION)\") ; \
				$$(call list_loop,TEST,$$(TESTS), \
					$$$$(call log,    $$$$(TEST)) ; \
						$$$$(call docker_make,$$$$(TEST)), \
					TRAVIS_FOLD \
				), \
			$$(call log_warning,Test \"$$(ROLE)\" on \"$$(DISTRIBUTION)\" is not supported) \
		) \
	)

test@test: .fail_if_host_not(test)
	$(call list_loop,TEST,$(TESTS), \
		$$(call log,Test \"$$(TEST)\") ; \
		$$(MAKE) $$(TEST) \
	)

TEST_HELP_LOCAL += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,test.debian.jessie, Test role - Debian Jessie))
test.debian.jessie: DISTRIBUTIONS = debian.jessie
test.debian.jessie: test@local

TEST_HELP_LOCAL += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,test.debian.stretch,Test role - Debian Stretch))
test.debian.stretch: DISTRIBUTIONS = debian.stretch
test.debian.stretch: test@local

TEST_HELP_LOCAL += $(call if_in,debian.buster,$(ROLE_DISTRIBUTIONS),$(call help,test.debian.buster, Test role - Debian Buster))
test.debian.buster: DISTRIBUTIONS = debian.buster
test.debian.buster: test@local
