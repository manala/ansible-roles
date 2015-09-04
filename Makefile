.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Package
PACKAGE_NAME        = oauth2-proxy
PACKAGE_DESCRIPTION = A reverse proxy that provides authentication with Google, Github or other provider
PACKAGE_VERSION     = 2.0.1
PACKAGE_RELEASE     = 3~elao
PACKAGE_GROUP       = web
PACKAGE_PROVIDES    = oauth2-proxy
PACKAGE_MAINTAINER  = infra@elao.com
PACKAGE_LICENSE     = MIT

## Package - Source
PACKAGE_SOURCE = https://github.com/bitly/oauth2_proxy.git

## Package - Release
PACKAGE_RELEASE_URL        = https://github.com/bitly/oauth2_proxy/releases/download
PACKAGE_RELEASE_GO_VERSION = 1.4.2

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
build: build-packages

build-packages:
	docker run \
	    --rm \
	    --volume `pwd`:/srv \
	    --workdir /srv \
	    --tty \
	    debian:wheezy \
	    sh -c '\
	        apt-get update && \
	        apt-get install -y make && \
	        make build-package@debian-wheezy \
	    '

build-package@debian-wheezy:
	apt-get install -y wget checkinstall
	# Get package
	wget --no-check-certificate ${PACKAGE_RELEASE_URL}/v${PACKAGE_VERSION}/oauth2_proxy-${PACKAGE_VERSION}.linux-amd64.go${PACKAGE_RELEASE_GO_VERSION}.tar.gz -O ~/package.tar.gz
	# Extract package
	mkdir -p ~/package
	tar xf ~/package.tar.gz -C ~/package --strip-components=1
	# Package description
	echo ${PACKAGE_DESCRIPTION} > ~/package/description-pak
	# Move binary
	mkdir -p ~/package/usr/bin
	mv ~/package/oauth2_proxy ~/package/usr/bin/oauth2-proxy
	# Copy package files
	cp -R build/package/* ~/package
	# File permissions
	chown -R root:root ~/package/etc ~/package/usr
	chmod +x ~/package/etc/init.d/*
	# Checkinstall
	cd ~/package && checkinstall \
	    -y \
	    --install=no \
	    --nodoc \
	    --include=include-files \
	    --pkgname=${PACKAGE_NAME} \
	    --pkgversion=${PACKAGE_VERSION} \
	    --pkgrelease=${PACKAGE_RELEASE} \
	    --pkggroup=${PACKAGE_GROUP} \
	    --provides=${PACKAGE_PROVIDES} \
	    --maintainer=${PACKAGE_MAINTAINER} \
	    --pkglicense=${PACKAGE_LICENSE} \
	    --pkgsource=${PACKAGE_SOURCE} \
	    true
	# Move package files
	mv ~/package/*.deb /srv/files
