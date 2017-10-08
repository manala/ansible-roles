.PHONY: sh update lint test

##########
# Manala #
##########

MANALA_DIR := $(abspath $(patsubst %/make/Makefile,%,$(firstword $(filter %.manala/make/Makefile,$(MAKEFILE_LIST)))))

include \
	$(MANALA_DIR)/make/Makefile.manala \
	$(MANALA_DIR)/make/Makefile.docker \
	$(MANALA_DIR)/make/Makefile.host \
	$(MANALA_DIR)/make/Makefile.travis

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

DISTRIBUTION_FAMILY  = $(call list_first,$(call list_split,.,$(DISTRIBUTION)))
DISTRIBUTION_RELEASE = $(call list_last,$(call list_split,.,$(DISTRIBUTION)))

##########
# Docker #
##########

MANALA_DOCKER_IMAGE       = manala/test-ansible
MANALA_DOCKER_IMAGE_TAG   = $(if $(ANSIBLE_VERSION),$(ANSIBLE_VERSION)-)$(DISTRIBUTION)
MANALA_DOCKER_DIR         = /srv/role
MANALA_DOCKER_HOST        = $(ROLE).$(DISTRIBUTION).test
MANALA_DOCKER_RUN_OPTIONS = --privileged
MANALA_DOCKER_VOLUMES     = \
	$(ROLE_DIR):/etc/ansible/roles/$(ROLE) \
	$(if $(CACHE_DIR), \
		$(call if_in,$(DISTRIBUTION_FAMILY),debian ubuntu, \
			$(CACHE_DIR)/$(DISTRIBUTION_FAMILY)/$(DISTRIBUTION_RELEASE)/apt/archives:/var/cache/apt/archives \
			$(CACHE_DIR)/$(DISTRIBUTION_FAMILY)/$(DISTRIBUTION_RELEASE)/apt/lists:/var/lib/apt/lists \
		) \
	)
MANALA_DOCKER_ENV         = \
	MANALA_HOST=test \
	MANALA_VERBOSE=$(MANALA_VERBOSE) \
	DISTRIBUTION=$(DISTRIBUTION) \
	DISTRIBUTION_FAMILY=$(DISTRIBUTION_FAMILY) \
	DISTRIBUTION_RELEASE=$(DISTRIBUTION_RELEASE) \
	ANSIBLE_SUDO_FLAGS="-H\ -S\ -n\ -E" \
	ANSIBLE_RETRY_FILES_ENABLED=0 \
	ANSIBLE_FORCE_COLOR=true

######
# Sh #
######

MANALA_HELP += $(call if_host,local,$(SH_HELP)\n)

SH_HELP = \
	$(call help_section,Test host shell)

sh: .host_restrict(local)
	$(call fail_unless,DISTRIBUTION)
	$(call if_in,$(DISTRIBUTION),$(ROLE_DISTRIBUTIONS), \
		$(call docker_shell), \
		$(call log_warning,Shell on \"$(DISTRIBUTION)\" is not supported) \
	)

SH_HELP += $(call if_in,debian.wheezy,$(ROLE_DISTRIBUTIONS),$(call help,sh.debian.wheezy, Open shell on test host - Debian Wheezy))
sh.debian.wheezy: DISTRIBUTION = debian.wheezy
sh.debian.wheezy: sh

SH_HELP += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,sh.debian.jessie, Open shell on test host - Debian Jessie))
sh.debian.jessie: DISTRIBUTION = debian.jessie
sh.debian.jessie: sh

SH_HELP += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,sh.debian.stretch,Open shell on test host - Debian Stretch))
sh.debian.stretch: DISTRIBUTION = debian.stretch
sh.debian.stretch: sh

SH_HELP += $(call if_in,centos.7,$(ROLE_DISTRIBUTIONS),$(call help,sh.centos.7,      Open shell on test host - CentOS 7))
sh.centos.7: DISTRIBUTION = centos.7
sh.centos.7: sh

SH_HELP += $(call if_in,ubuntu.xenial,$(ROLE_DISTRIBUTIONS),$(call help,sh.ubuntu.xenial, Open shell on test host - Ubuntu Xenial))
sh.ubuntu.xenial: DISTRIBUTION = ubuntu.xenial
sh.ubuntu.xenial: sh

##########
# Update #
##########

MANALA_HELP += $(call if_host,local,$(UPDATE_HELP)\n)

UPDATE_HELP = \
	$(call help_section,Test host update) \
	$(call help,update,               Update test hosts across distributions)

update: .host_restrict(local)
	$(call list_loop,DISTRIBUTION,$(if $(DISTRIBUTIONS),$(DISTRIBUTIONS),$(ROLE_DISTRIBUTIONS)), \
		$$(call if_in,$$(DISTRIBUTION),$$(ROLE_DISTRIBUTIONS), \
			$$(call log,Update \"$$(DISTRIBUTION)\") ; \
				$$(call docker_pull), \
			$$(call log_warning,Update \"$$(DISTRIBUTION)\" is not supported) \
		) \
	)

UPDATE_HELP += $(call if_in,debian.wheezy,$(ROLE_DISTRIBUTIONS),$(call help,update.debian.wheezy, Update test host - Debian Wheezy))
update.debian.wheezy: DISTRIBUTIONS = debian.wheezy
update.debian.wheezy: update

UPDATE_HELP += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,update.debian.jessie, Update test host - Debian Jessie))
update.debian.jessie: DISTRIBUTIONS = debian.jessie
update.debian.jessie: update

UPDATE_HELP += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,update.debian.stretch,Update test host - Debian Stretch))
update.debian.stretch: DISTRIBUTIONS = debian.stretch
update.debian.stretch: update

UPDATE_HELP += $(call if_in,centos.7,$(ROLE_DISTRIBUTIONS),$(call help,update.centos.7,      Update test host - CentOS 7))
update.centos.7: DISTRIBUTIONS = centos.7
update.centos.7: update

UPDATE_HELP += $(call if_in,ubuntu.xenial,$(ROLE_DISTRIBUTIONS),$(call help,update.ubuntu.xenial, Update test host - Ubuntu Xenial))
update.ubuntu.xenial: DISTRIBUTIONS = ubuntu.xenial
update.ubuntu.xenial: update

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

lint@local: .host_restrict(local)
	$(call list_loop,DISTRIBUTION,$(if $(DISTRIBUTIONS),$(DISTRIBUTIONS),$(ROLE_DISTRIBUTIONS)), \
		$$(call if_in,$$(DISTRIBUTION),$$(ROLE_DISTRIBUTIONS), \
			$$(call log,Lint \"$$(ROLE)\" on \"$$(DISTRIBUTION)\") ; \
				$$(call docker_make,lint@test), \
			$$(call log_warning,Lint \"$$(ROLE)\" on \"$$(DISTRIBUTION)\" is not supported) \
		) \
	)

lint@test: .host_restrict(test)
	ansible-lint --force-color -v $(ROLE_DIR)

LINT_HELP_LOCAL += $(call if_in,debian.wheezy,$(ROLE_DISTRIBUTIONS),$(call help,lint.debian.wheezy, Lint role - Debian Wheezy))
lint.debian.wheezy: DISTRIBUTIONS = debian.wheezy
lint.debian.wheezy: lint@local

LINT_HELP_LOCAL += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,lint.debian.jessie, Lint role - Debian Jessie))
lint.debian.jessie: DISTRIBUTIONS = debian.jessie
lint.debian.jessie: lint@local

LINT_HELP_LOCAL += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,lint.debian.stretch,Lint role - Debian Stretch))
lint.debian.stretch: DISTRIBUTIONS = debian.stretch
lint.debian.stretch: lint@local

LINT_HELP_LOCAL += $(call if_in,centos.7,$(ROLE_DISTRIBUTIONS),$(call help,lint.centos.7,      Lint role - CentOS 7))
lint.centos.7: DISTRIBUTIONS = centos.7
lint.centos.7: lint@local

LINT_HELP_LOCAL += $(call if_in,ubuntu.xenial,$(ROLE_DISTRIBUTIONS),$(call help,lint.ubuntu.xenial, Lint role - Ubuntu Xenial))
lint.ubuntu.xenial: DISTRIBUTIONS = ubuntu.xenial
lint.ubuntu.xenial: lint@local

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
	$(call verbose, ,ANSIBLE_STDOUT_CALLBACK=actionable, ) \
		ansible-playbook $@ --extra-vars="test=$(subst .yml,,$(subst tests/,,$@))"
FORCE:

MANALA_HELP += $(call if_host,local,$(TEST_HELP_LOCAL),$(TEST_HELP_TEST))

TEST_HELP       = $(call help_section,Test)
TEST_HELP_LOCAL = $(TEST_HELP) \
	$(call help,test,               Test role across distributions)
TEST_HELP_BUILD = $(TEST_HELP) \
	$(call help,test,Test role)

test: .host_switch(test)

test@local: .host_restrict(local)
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

test@test: .host_restrict(test)
	$(call list_loop,TEST,$(TESTS), \
		$$(call log,Test \"$$(TEST)\") ; \
		$$(MAKE) $$(TEST) \
	)

TEST_HELP_LOCAL += $(call if_in,debian.wheezy,$(ROLE_DISTRIBUTIONS),$(call help,test.debian.wheezy, Test role - Debian Wheezy))
test.debian.wheezy: DISTRIBUTIONS = debian.wheezy
test.debian.wheezy: test@local

TEST_HELP_LOCAL += $(call if_in,debian.jessie,$(ROLE_DISTRIBUTIONS),$(call help,test.debian.jessie, Test role - Debian Jessie))
test.debian.jessie: DISTRIBUTIONS = debian.jessie
test.debian.jessie: test@local

TEST_HELP_LOCAL += $(call if_in,debian.stretch,$(ROLE_DISTRIBUTIONS),$(call help,test.debian.stretch,Test role - Debian Stretch))
test.debian.stretch: DISTRIBUTIONS = debian.stretch
test.debian.stretch: test@local

TEST_HELP_LOCAL += $(call if_in,centos.7,$(ROLE_DISTRIBUTIONS),$(call help,test.centos.7,      Test role - CentOS 7))
test.centos.7: DISTRIBUTIONS = centos.7
test.centos.7: test@local

TEST_HELP_LOCAL += $(call if_in,ubuntu.xenial,$(ROLE_DISTRIBUTIONS),$(call help,test.ubuntu.xenial, Test role - Ubuntu Xenial))
test.ubuntu.xenial: DISTRIBUTIONS = ubuntu.xenial
test.ubuntu.xenial: test@local
