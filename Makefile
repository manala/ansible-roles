.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Role
ROLE_NAME = manala.grafana

## Macros
DOCKER = docker run \
    --rm \
    --volume `pwd`:/etc/ansible/roles/${ROLE_NAME} \
    --volume `pwd`:/srv \
    --cap-add SYS_PTRACE \
    --workdir /srv \
	--tty \
	-p 3002:3002 \
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

## Run dev container on debian wheezy
dev@wheezy: DEBIAN_DISTRIBUTION = wheezy
dev@wheezy: DOCKER_OPTIONS      = --interactive
dev@wheezy: DOCKER_COMMAND      = /bin/bash
dev@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

## Run dev container on debian jesssie
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
	ansible-lint -v .

########
# Test #
########

## Run tests on debian wheezy
test@wheezy: DEBIAN_DISTRIBUTION = wheezy
test@wheezy: DOCKER_COMMAND      = sh -c 'make test'
test@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

## Run tests on debian jessie
test@jessie: DEBIAN_DISTRIBUTION = jessie
test@jessie: DOCKER_COMMAND      = sh -c 'make test'
test@jessie:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

test: test-main

test-main:
	ansible-playbook tests/install.yml --syntax-check
	ansible-playbook tests/install.yml
	ansible-playbook tests/datasources.yml --syntax-check
	ansible-playbook tests/datasources.yml
	ansible-playbook tests/dashboards.yml --syntax-check
	ansible-playbook tests/dashboards.yml
