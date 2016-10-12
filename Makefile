.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Role
ROLE_NAME = manala.php

## Macros
DOCKER = docker run \
    --rm \
    --volume `pwd`:/etc/ansible/roles/${ROLE_NAME} \
    --volume `pwd`:/srv \
    --workdir /srv \
    --tty \
    --cap-add SYS_PTRACE \
    ${DOCKER_OPTIONS} \
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

dev@wheezy: DEBIAN_DISTRIBUTION = wheezy
dev@wheezy: DOCKER_OPTIONS      = --interactive
dev@wheezy: DOCKER_COMMAND      = /bin/bash
dev@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

dev@jessie: DEBIAN_DISTRIBUTION = jessie
dev@jessie: DOCKER_OPTIONS      = --interactive
dev@jessie: DOCKER_COMMAND      = /bin/bash
dev@jessie:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

########
# Lint #
########

lint@wheezy: DEBIAN_DISTRIBUTION = wheezy
lint@wheezy: DOCKER_COMMAND      = make lint
lint@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

lint@jessie: DEBIAN_DISTRIBUTION = jessie
lint@jessie: DOCKER_COMMAND      = make lint
lint@jessie:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

lint:
	ansible-lint -v -x deprecated .

########
# Test #
########

test@wheezy: DEBIAN_DISTRIBUTION = wheezy
test@wheezy: DOCKER_COMMAND      = sh -c 'make test'
test@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

test@jessie: DEBIAN_DISTRIBUTION = jessie
test@jessie: DOCKER_COMMAND      = sh -c 'make test'
test@jessie:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

test: test-install test-install-exclusive test-extensions test-configs-global test-configs test-fpm-pools test-blackfire test-services test-applications

test-install:
	ansible-playbook tests/install.yml --syntax-check
	ansible-playbook tests/install.yml

test-install-exclusive:
	ansible-playbook tests/install_exclusive.yml --syntax-check
	ansible-playbook tests/install_exclusive.yml

test-extensions:
	ansible-playbook tests/extensions.yml --syntax-check
	ansible-playbook tests/extensions.yml

test-configs-global:
	ansible-playbook tests/configs_global.yml --syntax-check
	ansible-playbook tests/configs_global.yml

test-configs:
	ansible-playbook tests/configs.yml --syntax-check
	ansible-playbook tests/configs.yml

test-fpm-pools:
	ansible-playbook tests/fpm_pools.yml --syntax-check
	ansible-playbook tests/fpm_pools.yml

test-blackfire:
	ansible-playbook tests/blackfire.yml --syntax-check
	ansible-playbook tests/blackfire.yml

test-services:
	ansible-playbook tests/services.yml --syntax-check
	ansible-playbook tests/services.yml

test-applications:
	ansible-playbook tests/applications.yml --syntax-check
	ansible-playbook tests/applications.yml
