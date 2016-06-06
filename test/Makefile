.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

ROLE_NAME     = manala.proftpd

## Macros
DOCKER = docker run \
    --rm \
    --volume `pwd`/..:/etc/ansible/roles/${ROLE_NAME} \
    --volume `pwd`:/srv/role \
    --workdir /srv/role \
    --tty \
    manala/ansible-debian:${DEBIAN_DISTRIBUTION} \
    make test-all DEBIAN_DISTRIBUTION=${DEBIAN_DISTRIBUTION}

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

########
# Test #
########

## Test on a jessie box
test@jessie: DEBIAN_DISTRIBUTION = jessie
test@jessie:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

test@wheezy: DEBIAN_DISTRIBUTION = wheezy
test@wheezy:
	printf "${COLOR_INFO}Run docker...${COLOR_RESET}\n"
	$(DOCKER)

check-syntax:
	printf "${COLOR_INFO}Syntax check running...${COLOR_RESET}\n"
	ansible-playbook test.yml --syntax-check --extra-vars "role_name=${ROLE_NAME}"

check-practices:
	printf "${COLOR_INFO}Practices check running...${COLOR_RESET}\n"
	ansible-lint -v .

check-provision:
	printf "${COLOR_INFO}Executing role...${COLOR_RESET}\n"
	ansible-playbook test.yml --extra-vars "role_name=${ROLE_NAME}"

check-server:
	printf "${COLOR_INFO}Validating server side...${COLOR_RESET}\n"
	goss validate

test-all: check-syntax check-practices check-provision check-server
