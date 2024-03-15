# Prerequisites:
#   - "container" environment variable in docker containers equal to "docker"
#   - "MANALA_DIR" make variable
#   - "MANALA_DOCKER_COMMAND" & "MANALA_DOCKER_COMMAND_SERVICE" make variables
#   - Mandatory include os.mk
#   - Mandatory .manala/docker/compose.yaml
#   - Optionals .manala/docker/compose/os.$(MANALA_OS).yaml
#   - Mandatory .manala/docker/compose/ssh-agent.yaml
#   - Mandatory .manala/docker/compose/docker.yaml
#   - Mandatory .manala/docker/compose/docker.cache.yaml
#   - Mandatory .manala/docker/compose/env.file.yaml
#   - Mandatory .manala/docker/compose/project.cache.yaml
#   - Mandatory .manala/docker/compose/profile.$(MANALA_DOCKER_COMPOSE_PROFILE).yaml if "MANALA_DOCKER_COMPOSE_PROFILE" make variable
#   - Optional include git.mk
#   - Mandatory .manala/docker/compose/git.yaml if include git.mk
#   - Mandatory .manala/docker/compose/github.yaml if include git.mk

##########
# Docker #
##########

ifeq ($(container),docker)
MANALA_DOCKER = 1
endif

MANALA_DOCKER_BIN = docker

MANALA_DOCKER_SOCK = /var/run/docker.sock

# Usage:
#   $(manala_docker) [COMMAND] [ARGS...]

define manala_docker
	$(MANALA_DOCKER_BIN)
endef

##################
# Docker Compose #
##################

MANALA_DOCKER_COMPOSE_BIN_DEFAULT = $(call manala_docker) compose

MANALA_DOCKER_COMPOSE_BIN = $(MANALA_DOCKER_COMPOSE_BIN_DEFAULT)

MANALA_HOST_USER_ID = $(shell id -u)
MANALA_HOST_GROUP_ID = $(shell id -g)

MANALA_DOCKER_COMPOSE_ENV = \
	DOCKER_BUILDKIT=1 \
	$(and $(MANALA_OS_LINUX), $(filter-out 0, $(MANALA_HOST_USER_ID)), \
		MANALA_USER_ID=$(MANALA_HOST_USER_ID) \
		MANALA_GROUP_ID=$(MANALA_HOST_GROUP_ID) \
	)

MANALA_DOCKER_COMPOSE_FILE = $(MANALA_DIR)/.manala/docker/compose.yaml

# Os
MANALA_DOCKER_COMPOSE_FILE_OS = $(MANALA_DIR)/.manala/docker/compose/os.$(MANALA_OS).yaml
MANALA_DOCKER_COMPOSE_FILE += $(if $(wildcard $(MANALA_DOCKER_COMPOSE_FILE_OS)), $(MANALA_DOCKER_COMPOSE_FILE_OS))

# Ssh
ifdef SSH_AUTH_SOCK
# See: https://docs.docker.com/desktop/mac/networking/#ssh-agent-forwarding
MANALA_DOCKER_COMPOSE_ENV += $(if $(MANALA_OS_DARWIN), \
	SSH_AUTH_SOCK=/run/host-services/ssh-auth.sock \
)
MANALA_DOCKER_COMPOSE_FILE += $(MANALA_DIR)/.manala/docker/compose/ssh.agent-bridge.yaml
endif

# Docker
MANALA_DOCKER_COMPOSE_ENV += MANALA_DOCKER_SOCK=$(MANALA_DOCKER_SOCK)
MANALA_DOCKER_COMPOSE_FILE += $(MANALA_DIR)/.manala/docker/compose/docker.bridge.yaml

# Docker - Cache
ifneq ($(and $(MANALA_DOCKER_CACHE_FROM),$(MANALA_DOCKER_CACHE_TO)),)
MANALA_DOCKER_COMPOSE_FILE += $(MANALA_DIR)/.manala/docker/compose/docker.cache.yaml
endif

# Git
MANALA_DOCKER_COMPOSE_ENV += \
	$(if $(MANALA_GIT_CONFIG), MANALA_GIT_CONFIG=$(MANALA_GIT_CONFIG)) \
	$(if $(MANALA_GITHUB_CONFIG), MANALA_GITHUB_CONFIG=$(MANALA_GITHUB_CONFIG))
MANALA_DOCKER_COMPOSE_FILE += \
	$(if $(MANALA_GIT_CONFIG), $(MANALA_DIR)/.manala/docker/compose/git.yaml) \
	$(if $(MANALA_GITHUB_CONFIG), $(MANALA_DIR)/.manala/docker/compose/github.yaml)

# Profile
MANALA_DOCKER_COMPOSE_FILE += \
	$(if $(MANALA_DOCKER_COMPOSE_PROFILE), $(MANALA_DIR)/.manala/docker/compose/profile.$(MANALA_DOCKER_COMPOSE_PROFILE).yaml)

# Env file
MANALA_DOCKER_COMPOSE_ENV += \
	$(if $(MANALA_DOCKER_ENV_FILE), MANALA_DOCKER_ENV_FILE=$(MANALA_DOCKER_ENV_FILE))
MANALA_DOCKER_COMPOSE_FILE += \
	$(if $(MANALA_DOCKER_ENV_FILE), $(MANALA_DIR)/.manala/docker/compose/env.file.yaml)

# Project cache
MANALA_DOCKER_COMPOSE_FILE += \
	$(if $(MANALA_DOCKER_PROJECT_CACHE), $(MANALA_DIR)/.manala/docker/compose/project.cache.yaml)

# Debug
MANALA_DOCKER_COMPOSE_ENV += $(if $(MANALA_DOCKER_DEBUG), BUILDKIT_PROGRESS=plain)

# Usage:
#   $(manala_docker_compose) [COMMAND] [ARGS...]

# Note: the `env` call MUST be kept for recent Make versions (>= 4.3)
# See: https://github.com/manala/manala-recipes/pull/270

define manala_docker_compose
	$(if $(MANALA_DOCKER_COMPOSE_ENV), env $(MANALA_DOCKER_COMPOSE_ENV)) \
	$(MANALA_DOCKER_COMPOSE_BIN) \
		$(if $(MANALA_DOCKER_COMPOSE_PROFILE), --profile $(MANALA_DOCKER_COMPOSE_PROFILE)) \
		$(foreach FILE, $(MANALA_DOCKER_COMPOSE_FILE), \
			--file $(FILE) \
		)
endef

ifndef MANALA_DOCKER

manala.docker.compose:
	$(manala_docker_compose) $(OPTIONS) $(COMMAND)

endif

###########
# Command #
###########

# GitHub Action
MANALA_DOCKER_COMMAND_ENV += \
	$(if $(GITHUB_ACTIONS), \
		CI="$${CI}" \
		GITHUB_ACTION="$${GITHUB_ACTION}" \
		GITHUB_ACTION_REF="$${GITHUB_ACTION_REF}" \
		GITHUB_ACTION_REPOSITORY="$${GITHUB_ACTION_REPOSITORY}" \
		GITHUB_ACTIONS="$${GITHUB_ACTIONS}" \
		GITHUB_ACTOR="$${GITHUB_ACTOR}" \
		GITHUB_JOB="$${GITHUB_JOB}" \
		GITHUB_WORKFLOW="$${GITHUB_WORKFLOW}" \
	)

# Usage:
#   $(manala_docker_command) [COMMAND] [ARGS...]
#   $(call manala_docker_command, [OPTIONS]) [COMMAND] [ARGS...]

define manala_docker_command
	$(manala_docker_compose) $(MANALA_DOCKER_COMMAND) \
		$(if $(MANALA_DOCKER_COMMAND_DIR), --workdir $(MANALA_DOCKER_COMMAND_DIR), \
			$(if $(MANALA_DOCKER_COMMAND_DEFAULT_DIR), --workdir $(MANALA_DOCKER_COMMAND_DEFAULT_DIR)) \
		) \
		$(foreach ENV, $(MANALA_DOCKER_COMMAND_ENV), \
			--env $(ENV) \
		) \
		$(1) \
		$(MANALA_DOCKER_COMMAND_SERVICE)
endef

################
# Shell / Make #
################

ifndef MANALA_DOCKER
define manala_docker_shell
	$(if $(2), \
		$(call manala_docker_command, $(strip $(1))) /bin/sh -c '$(subst ','\'',$(strip $(2)))', \
		$(call manala_docker_command,) /bin/sh -c '$(subst ','\'',$(strip $(1)))' \
	)
endef
MANALA_DOCKER_SHELL = $(manala_docker_command) /bin/sh
MANALA_DOCKER_MAKE = $(manala_docker_command) make
else
define manala_docker_shell
	$(if $(2), \
		$(call message_error, Unable to run docker shell command with options inside a docker container) ; exit 1 ;, \
		$(strip $(1)) \
	)	
endef
MANALA_DOCKER_SHELL := $(SHELL)
MANALA_DOCKER_MAKE := $(MAKE)
endif
