.SILENT:
.PHONY: help build test split

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

# Git
GIT_REPOSITORIES_DELTA = ${shell git diff --name-only ${TRAVIS_COMMIT_RANGE} | grep "/" | cut -d "/" -f1 | sort -u | tr "\n" " "}
ifeq (${GIT_REPOSITORIES_DELTA},)
GIT_REPOSITORIES = ${wildcard */}
else
GIT_REPOSITORIES = ${GIT_REPOSITORIES_DELTA}
endif

# Help
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

#########
# Build #
#########

## Build
build:
	EXIT=0 ; ${foreach \
		repository,\
		${GIT_REPOSITORIES},\
		printf "\n${COLOR_INFO}Build ${COLOR_COMMENT}${repository}${COLOR_RESET}\n\n" && ${MAKE} --directory=${repository} build || EXIT=$$? ;\
	} exit $$EXIT

#########
# Test #
#########

## Test
test:
	EXIT=0 ; ${foreach \
		repository,\
		${GIT_REPOSITORIES},\
		printf "\n${COLOR_INFO}Test ${COLOR_COMMENT}${repository}${COLOR_RESET}\n\n" && ${MAKE} --directory=${repository} test || EXIT=$$? ;\
	} exit $$EXIT

#########
# Split #
#########

## Split
split:
ifeq (${shell uname -s},Darwin)
	docker run \
		--rm \
		--tty --interactive \
		--volume ${PWD}:/srv \
		--volume ${HOME}/.ssh:/root/.ssh \
		jderusse/gitsplit
else
	docker run \
		--rm \
		--tty --interactive \
		--volume ${PWD}:/srv \
		--volume ${SSH_AUTH_SOCK}:/ssh-agent \
		--env SSH_AUTH_SOCK=/ssh-agent \
		jderusse/gitsplit
endif
