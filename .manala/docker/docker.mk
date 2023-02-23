# Prerequisites:
#   - "container" environment variable in docker containers equal to "docker"
#   - "MANALA_DIR" make variable
#   - "manala_docker_command" make function
#   - Mandatory include os.mk
#   - Mandatory .manala/docker/compose.yaml
#   - Optionals .manala/docker/compose/os.$(MANALA_OS).yaml
#   - Mandatory .manala/docker/compose/ssh-agent.yaml
#   - Mandatory .manala/docker/compose/docker.yaml
#   - Mandatory .manala/docker/compose/docker.cache.yaml
#   - Mandatory .manala/docker/compose/profile.$(MANALA_DOCKER_COMPOSE_PROFILE).yaml if "MANALA_DOCKER_COMPOSE_PROFILE" make variable
#   - Optional include git.mk
#   - Mandatory .manala/docker/compose/git.yaml if include git.mk
#   - Mandatory .manala/docker/compose/github.yaml if include git.mk

ifeq ($(container),docker)
MANALA_DOCKER = 1
endif

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

##########
# Docker #
##########

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

MANALA_DOCKER_COMPOSE_BIN_DEFAULT = $(MANALA_DOCKER_BIN) compose

MANALA_DOCKER_COMPOSE_BIN = $(MANALA_DOCKER_COMPOSE_BIN_DEFAULT)

MANALA_DOCKER_COMPOSE_ENV = \
	DOCKER_BUILDKIT=1 \
	$(if $(MANALA_OS_LINUX), \
		MANALA_USER_ID=$(shell id -u) \
		MANALA_GROUP_ID=$(shell id -g) \
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
	MANALA_SSH_AUTH_SOCK_BIND=/run/host-services/ssh-auth.sock.bind \
)
MANALA_DOCKER_COMPOSE_FILE += $(MANALA_DIR)/.manala/docker/compose/ssh-agent.yaml
endif

# Docker
MANALA_DOCKER_COMPOSE_ENV += \
	MANALA_DOCKER_SOCK=/var/run/docker.sock \
	MANALA_DOCKER_SOCK_BIND=/var/run/docker.sock.bind
MANALA_DOCKER_COMPOSE_FILE += $(MANALA_DIR)/.manala/docker/compose/docker.yaml

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

# Debug
ifdef DEBUG
MANALA_DOCKER_COMPOSE_ENV += BUILDKIT_PROGRESS=plain
endif

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
