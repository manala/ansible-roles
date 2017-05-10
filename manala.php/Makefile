.SILENT:
.PHONY: help dev lint test tests

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m
COLOR_ERROR   = \033[31m

## Ansible
ANSIBLE_ROLE     = manala.php
ANSIBLE_VERSION ?=

export ANSIBLE_FORCE_COLOR = true

## Debian
DEBIAN_DISTRIBUTION ?= wheezy jessie

# Docker
DOCKER_IMAGE = manala/ansible-debian
DOCKER_TAG  ?=

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

## Dev
dev:
	docker run \
		--rm \
		--volume `pwd`:/etc/ansible/roles/${ANSIBLE_ROLE} \
		--volume `pwd`:/srv \
		--workdir /srv \
		--tty --interactive \
		--privileged \
		--env USER_ID=`id -u` \
		--env GROUP_ID=`id -g` \
		${DOCKER_IMAGE}:$(if ${DOCKER_TAG},${DOCKER_TAG}-)$(lastword ${DEBIAN_DISTRIBUTION})

## Dev - Wheezy
dev@wheezy: DEBIAN_DISTRIBUTION = wheezy
dev@wheezy: dev

## Dev - Jessie
dev@jessie: DEBIAN_DISTRIBUTION = jessie
dev@jessie: dev

########
# Lint #
########

## Lint
lint:
	printf "${COLOR_INFO}Lint${COLOR_RESET}\n\n"
	docker run \
		--rm \
		--volume `pwd`:/srv \
		--workdir /srv \
		${DOCKER_IMAGE}:$(if ${DOCKER_TAG},${DOCKER_TAG}-)$(lastword ${DEBIAN_DISTRIBUTION}) \
		ansible-lint --force-color -v .

########
# Test #
########

## Test
test:
	EXIT=0 ; ${foreach \
		distribution,\
		${DEBIAN_DISTRIBUTION},\
		printf "\n${COLOR_INFO}Test ${COLOR_COMMENT}${distribution}${COLOR_RESET}\n\n" && \
			docker run \
				--rm \
				--volume `pwd`:/etc/ansible/roles/${ANSIBLE_ROLE} \
				--volume `pwd`:/srv \
				--workdir /srv \
				${DOCKER_IMAGE}:$(if ${DOCKER_TAG},${DOCKER_TAG}-)${distribution} \
				make tests \
		|| EXIT=$$? ;\
	} exit $$EXIT

TESTS = ${sort \
	${foreach \
		test,\
		${wildcard tests/*.yml},\
		${if ${findstring .goss.,${test}},,${test}}\
	}\
}

## Tests
tests:
	EXIT=0 ; ${foreach \
		test,\
		${TESTS},\
		make ${test} || EXIT=$$? ;\
	} exit $$EXIT

tests/%.yml: FORCE
	ansible-playbook $@ --extra-vars="test=${subst .yml,,${subst tests/,,$@}}"
FORCE:

## Test - Wheezy
test@wheezy: DEBIAN_DISTRIBUTION = wheezy
test@wheezy: test

## Test - Jessie
test@jessie: DEBIAN_DISTRIBUTION = jessie
test@jessie: test
