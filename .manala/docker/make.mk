##########
# Docker #
##########

# Internal usage:
#   $(_docker) [COMMAND] [ARGS...]

ifneq ($(container),docker)
define _docker
	docker
endef
else
define _docker
	$(call message_error, Unable to execute command inside a docker container) ; \
		exit 1 ;
endef
endif

##################
# Docker Compose #
##################

_DOCKER_COMPOSE = $(shell which docker) compose
_DOCKER_COMPOSE_ENV = \
	DOCKER_BUILDKIT=1 \
	DIR=/srv/ansible_collections/manala/roles \
	CACHE_DIR=/srv/ansible_collections/manala/roles/$(shell dir=$(_DIR)/$(_CACHE_DIR) ; mkdir -p $${dir} ; echo $(_CACHE_DIR)) \
	USER_ID=$(shell id -u) \
	GROUP_ID=$(shell id -g)
_DOCKER_COMPOSE_FILE = \
	$(_DIR)/.manala/docker/compose.yaml \
	$(_DIR)/.manala/docker/compose/os.$(OS).yaml
_DOCKER_COMPOSE_SERVICE = system
_DOCKER_COMPOSE_USER = lazy

# Debug
ifdef DEBUG
_DOCKER_COMPOSE_ENV += BUILDKIT_PROGRESS=plain
endif

# Ssh Agent
ifdef SSH_AUTH_SOCK
_DOCKER_COMPOSE_FILE += $(_DIR)/.manala/docker/compose/ssh-agent.yaml
	# See: https://docs.docker.com/desktop/mac/networking/#ssh-agent-forwarding
	ifdef OS_DARWIN
_DOCKER_COMPOSE_ENV += SSH_AUTH_SOCK=/run/host-services/ssh-auth.sock
_DOCKER_COMPOSE_ENV += MANALA_SSH_AUTH_SOCK_BIND=/run/host-services/ssh-auth.sock.bind
	endif
endif

# Docker
_DOCKER_COMPOSE_FILE += $(_DIR)/.manala/docker/compose/docker.yaml
_DOCKER_COMPOSE_ENV += MANALA_DOCKER_SOCK=/var/run/docker.sock
_DOCKER_COMPOSE_ENV += MANALA_DOCKER_SOCK_BIND=/var/run/docker.sock.bind

# Internal usage:
#   $(_docker_compose) [COMMAND] [ARGS...]

ifneq ($(container),docker)
define _docker_compose
	$(_DOCKER_COMPOSE_ENV) \
	$(_DOCKER_COMPOSE) \
		$(foreach file, $(_DOCKER_COMPOSE_FILE), \
			--file $(file) \
		)
endef
else
define _docker_compose
	$(call message_error, Unable to execute command inside a docker container) ; \
		exit 1 ;
endef
endif

###########
# Helpers #
###########

# Usage:
#   $(call docker_run, COMMAND [ARGS...])
#   $(call docker_run, OPTIONS, COMMAND [ARGS...])

ifneq ($(container),docker)
define docker_run
	$(_docker_compose) run \
		--rm \
		$(if $(strip $(2)), \
			$(strip $(1)) $(_DOCKER_COMPOSE_SERVICE) sh -c '$(strip $(2))', \
			$(_DOCKER_COMPOSE_SERVICE) sh -c '$(subst ','\'',$(strip $(1)))' \
		)
endef
else
define docker_run
	$(if $(strip $(2)), \
		$(call message_error, Unable to execute command inside a docker container) ; exit 1 ;, \
		$(strip $(1)) \
	)
endef
endif

# Usage:
#   $(docker_exec) [COMMAND] [ARGS...]

ifneq ($(container),docker)
define docker_exec
	$(_docker_compose) exec \
		$(if $(_DOCKER_COMPOSE_USER),--user $(_DOCKER_COMPOSE_USER)) \
		$(_DOCKER_COMPOSE_SERVICE) \
		sh -c '$(strip $(1))'
endef
else
define docker_exec
	$(strip $(1))
endef
endif
