# Relative root dir ("."|".."|"../.."|…)
_DIR := $(patsubst ./%,%,$(patsubst %/.manala/Makefile,%,./$(filter %.manala/Makefile,$(MAKEFILE_LIST))))
# Is current dir root ? (""|"1")
_ROOT = $(if $(filter .,$(_DIR)),1)
# Relative current dir ("."|"foo"|"foo/bar"|…)
_CURRENT_DIR = $(patsubst ./%,%,.$(patsubst $(realpath $(CURDIR)/$(_DIR))%,%,$(CURDIR)))
# Cache dir
_CACHE_DIR = .manala/.cache

include $(_DIR)/.manala/make/text.mk
include $(_DIR)/.manala/make/help.mk
include $(_DIR)/.manala/make/os.mk
include $(_DIR)/.manala/docker/make.mk

##########
# System #
##########

ifneq ($(container),docker)

HELP += $(call help_section, System)

HELP += $(call help,sh,   Open a local system shell)
sh:
	$(call docker_run, exec bash --login)
.PHONY: sh

HELP += $(call help,clean,Clean local system)
clean:
	@$(call confirm, Confirm system cleaning)
	@$(call log, Stops and removes docker containers$(,) networks$(,) volumes$(,) images…)
	$(_docker_compose) down \
		--rmi all \
		--volumes \
		--remove-orphans
	@$(call log, Removes old docker images…)
	$(_docker) images \
		--filter reference='manala-ansible-roles:*' \
		--format "{{.ID}}" \
			| xargs $(_docker) rmi --force
	@$(call log, Delete cache dir…)
	rm -Rf $(_DIR)/$(_CACHE_DIR)
.PHONY: clean

endif
