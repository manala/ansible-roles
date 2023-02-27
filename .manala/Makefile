# Project root dir, relative to current dir (.|..|../..|…)
MANALA_DIR := $(patsubst %/.,%,$(patsubst %.manala/..,%.,$(patsubst %Makefile,%..,$(lastword $(MAKEFILE_LIST)))))
# Current dir, relative to project root dir (.|dir|dir/dir|…)
MANALA_CURRENT_DIR = $(patsubst ./%,%,.$(patsubst $(realpath $(CURDIR)/$(MANALA_DIR))%,%,$(CURDIR)))
# Is current dir root ? (|1)
MANALA_CURRENT_ROOT = $(if $(filter .,$(MANALA_CURRENT_DIR)),1)
# Cache dir, relative to project dir
MANALA_CACHE_DIR = .manala/.cache

###########
# Project #
###########

include $(MANALA_DIR)/.manala/make/text.mk
include $(MANALA_DIR)/.manala/make/help.mk
include $(MANALA_DIR)/.manala/make/os.mk
include $(MANALA_DIR)/.manala/docker/docker.mk

##########
# Docker #
##########

MANALA_DOCKER_COMPOSE_ENV += \
	MANALA_DIR=/srv/ansible_collections/manala/roles \
	MANALA_CACHE_DIR=/srv/ansible_collections/manala/roles/$(shell dir=$(MANALA_DIR)/$(MANALA_CACHE_DIR) ; mkdir -p $${dir} ; echo $(MANALA_CACHE_DIR))

define manala_docker_command
	$(manala_docker_compose) run \
		--rm \
		$(1) \
		system
endef

##########
# System #
##########

# Docker commands only available *OUTSIDE* docker environment
ifndef MANALA_DOCKER

MANALA_HELP += $(call manala_help_section, System)

MANALA_HELP += $(call manala_help,sh,   Open a local system shell)
sh:
	$(manala_docker_command) bash --login
.PHONY: sh

MANALA_HELP += $(call manala_help,clean,Clean local system)
clean:
	@$(call manala_confirm, Confirm system cleaning)
	@$(call manala_log, Stops and removes docker containers$(,) networks$(,) volumes$(,) images…)
	$(manala_docker_compose) down \
		--rmi all \
		--volumes \
		--remove-orphans
	@$(call manala_log, Removes old docker images…)
	$(manala_docker) images \
		--filter reference='manala-ansible-roles:*' \
		--format "{{.ID}}" \
			| xargs $(manala_docker) rmi --force
	@$(call manala_log, Delete cache dir…)
	rm -Rf $(MANALA_DIR)/$(MANALA_CACHE_DIR)
.PHONY: clean

endif
