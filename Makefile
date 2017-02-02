.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Role
ROLE_NAME = manala.files

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

test: test-attributes

test-attributes: test-attributes-template test-attributes-content test-attributes-copy test-attributes-url test-attributes-file test-attributes-directory test-attributes-file test-attributes-link test-attributes-override test-attributes-link-directory test-attributes-defaults

test-attributes-template:
	ansible-playbook tests/attributes_template.yml --syntax-check
	ansible-playbook tests/attributes_template.yml

test-attributes-content:
	ansible-playbook tests/attributes_content.yml --syntax-check
	ansible-playbook tests/attributes_content.yml

test-attributes-copy:
	ansible-playbook tests/attributes_copy.yml --syntax-check
	ansible-playbook tests/attributes_copy.yml

test-attributes-url:
	ansible-playbook tests/attributes_url.yml --syntax-check
	ansible-playbook tests/attributes_url.yml

test-attributes-file:
	ansible-playbook tests/attributes_file.yml --syntax-check
	ansible-playbook tests/attributes_file.yml

test-attributes-directory:
	ansible-playbook tests/attributes_directory.yml --syntax-check
	ansible-playbook tests/attributes_directory.yml

test-attributes-link:
	ansible-playbook tests/attributes_link.yml --syntax-check
	ansible-playbook tests/attributes_link.yml

test-attributes-override:
	ansible-playbook tests/attributes_override.yml --syntax-check
	ansible-playbook tests/attributes_override.yml

test-attributes-link-directory:
	ansible-playbook tests/attributes_link_directory.yml --syntax-check
	ansible-playbook tests/attributes_link_directory.yml

test-attributes-link-file:
	ansible-playbook tests/attributes_link_file.yml --syntax-check
	ansible-playbook tests/attributes_link_file.yml

test-attributes-defaults:
	ansible-playbook tests/attributes_defaults.yml --syntax-check
	ansible-playbook tests/attributes_defaults.yml
