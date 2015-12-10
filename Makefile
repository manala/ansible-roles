.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Package
PACKAGE_NAME        = mailhog
PACKAGE_DESCRIPTION = Web and API based SMTP testing
PACKAGE_VERSION     = 0.1.8
PACKAGE_RELEASE     = elao1
PACKAGE_LICENSE     = MIT
PACKAGE_HOMEPAGE    = https://github.com/mailhog/MailHog

PACKAGE_MAINTAINER  = "Elao Infra <infra@elao.com>"

## Package - Source
PACKAGE_SOURCE = https://github.com/mailhog/MailHog/releases/download

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

## Build
build: build@debian-jessie

build@debian-jessie:
	docker run \
	    --rm \
	    --volume `pwd`:/srv \
	    --workdir /srv \
	    --tty \
	    debian:jessie \
	    sh -c '\
	        apt-get update && \
	        apt-get install -y make && \
	        make build-package@debian-jessie \
	    '

build-package@debian-jessie:
	# Fpm (prefer git version, as 1.4 don't support systemd options)
	apt-get -y install git ruby ruby-dev gcc xz-utils
	git clone https://github.com/jordansissel/fpm.git ~/fpm
	cd ~/fpm && git checkout e02526e
	cd ~/fpm && make install
	# Dependencies
	apt-get -y install wget
	# Get binary
	mkdir -p ~/package/usr/bin
	wget ${PACKAGE_SOURCE}/v${PACKAGE_VERSION}/MailHog_linux_amd64 -O ~/package/usr/bin/mailhog
	chmod 755 ~/package/usr/bin/mailhog
	# Fpm
	cd ~/package && fpm \
	    --verbose \
	    -s dir \
	    -t deb \
	    --deb-compression xz \
	    -n ${PACKAGE_NAME} \
	    -v ${PACKAGE_VERSION} \
	    --iteration ${PACKAGE_RELEASE} \
	    -m ${PACKAGE_MAINTAINER} \
	    --description "${PACKAGE_DESCRIPTION}" \
	    --license ${PACKAGE_LICENSE} \
	    --url ${PACKAGE_HOMEPAGE} \
	    --deb-systemd "/srv/build/systemd/mailhog" \
	    --vendor "" \
	    .
	# Move package files
	mv ~/package/*.deb /srv/files/debian_jessie
