.SILENT:
.PHONY: help dev lint test

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Ansible
ANSIBLE_ROLE     = manala.rsyslog
ANSIBLE_VERSION ?=

## Debian
DEBIAN_DISTRIBUTION ?= jessie

## Docker
DOCKER_OPTIONS =
DOCKER = docker run \
    --rm \
    --volume `pwd`:/etc/ansible/roles/${ANSIBLE_ROLE} \
    --volume `pwd`:/srv \
    --workdir /srv \
    --tty \
    --privileged \
    ${DOCKER_OPTIONS} \
    manala/ansible-debian:${if ${ANSIBLE_VERSION},${ANSIBLE_VERSION}-}${DEBIAN_DISTRIBUTION}

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
	{ lastLine = $$0 }' ${MAKEFILE_LIST}

#######
# Dev #
#######

## Dev - Wheezy
dev@wheezy: DEBIAN_DISTRIBUTION = wheezy
dev@wheezy: dev

## Dev - Jessie
dev@jessie: DEBIAN_DISTRIBUTION = jessie
dev@jessie: dev

## Dev
dev: DOCKER_OPTIONS = --interactive
dev:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	${DOCKER} /bin/bash

########
# Lint #
########

## Lint
lint:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	${DOCKER} ansible-lint -v -x deprecated .

########
# Test #
########

test@wheezy: DEBIAN_DISTRIBUTION = wheezy
test@wheezy: test

test@jessie: DEBIAN_DISTRIBUTION = jessie
test@jessie: test

TESTS = ${sort \
	${foreach \
		test,\
		${wildcard tests/*.yml},\
		${if ${findstring .goss.,${test}},,${test}}\
	}\
}

## Test
test:
	EXIT=0 ; ${foreach \
		test,\
		${TESTS},\
		printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n" && ${DOCKER} sh -c 'make ${test}' || EXIT=$$? ;\
	} exit $$EXIT

tests/%.yml: FORCE
	ansible-playbook $@ --extra-vars="test=${subst .yml,,${subst tests/,,$@}}"
FORCE:
