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

# Command
MANALA_DOCKER_COMMAND = run --rm
MANALA_DOCKER_COMMAND_SERVICE = system

##########
# System #
##########

# Docker commands only available *OUTSIDE* docker environment
ifndef MANALA_DOCKER

MANALA_HELP += $(call manala_help_section, System)

MANALA_HELP += $(call manala_help,sh,   Shell to local system (DIR|PORT|DEBUG))
sh: MANALA_DOCKER_COMMAND_DIR ?= $(if $(findstring command line,$(origin DIR)),$(DIR))
sh: MANALA_DOCKER_DEBUG = $(if $(DEBUG),1)
sh:
	if [ ! -t 0 ] ; then \
		$(call manala_docker_command, \
			--no-TTY \
			$(if $(PORT),--publish $(PORT)), \
		) sh -s ; \
	else \
		$(call manala_docker_command, \
			$(if $(PORT),--publish $(PORT)), \
		) bash --login ; \
	fi
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
			| xargs -r $(manala_docker) rmi --force
	@$(call manala_log, Delete cache dir…)
	rm -Rf $(MANALA_DIR)/$(MANALA_CACHE_DIR)
.PHONY: clean

endif
