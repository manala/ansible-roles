.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Role
ROLE_NAME = manala.apt

## Macros
DOCKER = docker run \
    --rm \
    --volume `pwd`:/etc/ansible/roles/${ROLE_NAME} \
    --volume `pwd`:/srv \
    --workdir /srv \
    --tty \
    --interactive \
    manala/ansible-debian:${DEBIAN_DISTRIBUTION} \
    ${DOCKER_COMMAND}

## Help
help:
	printf "${COLOR_COMMENT}Usage:${COLOR_RESET}\n"
	printf " make [target]\n\n"
	printf "${COLOR_COMMENT}Available targets:${COLOR_RESET}\n"
	awk '/^[a-zA-Z\-\_0-9\.@]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf " ${COLOR_INFO}%-16s${COLOR_RESET} %s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

#######
# Dev #
#######

dev@jessie: DEBIAN_DISTRIBUTION = jessie
dev@jessie: DOCKER_COMMAND      = /bin/bash
dev@jessie:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

dev@wheezy: DEBIAN_DISTRIBUTION = wheezy
dev@jessie: DOCKER_COMMAND      = /bin/bash
dev@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

#########
# Tests #
#########

test-dependencies:
	ansible-playbook tests/dependencies.yml

test-sources-list:
	ansible-playbook tests/sources_list.yml

test-preferences:
	ansible-playbook tests/preferences.yml

test-repositories:
	ansible-playbook tests/repositories.yml

test-keys:
	ansible-playbook tests/keys.yml
