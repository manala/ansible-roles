.SILENT:
.PHONY: help

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Package
PACKAGE_VERSION = 0.10.2

## Package - Source
PACKAGE_SOURCE = http://www.mirrorservice.org/sites/dl.sourceforge.net/pub/sourceforge/p/pa/pamsshagentauth/pam_ssh_agent_auth

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
build: build@debian-wheezy build@debian-jessie build@ubuntu-trusty

build@debian-wheezy:
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

build@ubuntu-trusty:
	docker run \
	    --rm \
	    --volume `pwd`:/srv \
	    --workdir /srv \
	    --tty \
	    ubuntu:trusty \
	    sh -c '\
	        apt-get update && \
	        apt-get install -y make && \
	        make build-package@ubuntu-trusty \
	    '

build-package@debian-wheezy:
	apt-get install -y wget build-essential debhelper autotools-dev libssl-dev libpam0g-dev devscripts
	# Get origin package
	wget ${PACKAGE_SOURCE}/v${PACKAGE_VERSION}/pam_ssh_agent_auth-${PACKAGE_VERSION}.tar.bz2 -O ~/package.tar.bz2
	# Extract origin package
	mkdir -p ~/package
	tar xfv ~/package.tar.bz2 -C ~/package --strip-components=1
	# Build package
	cd ~/package && debuild -i -us -uc -b
	# Move package files
	rm -f /srv/files/debian_wheezy/*.deb
	mv ~/*.deb /srv/files/debian_wheezy

build-package@debian-jessie:
	apt-get install -y wget build-essential debhelper autotools-dev libssl-dev libpam0g-dev devscripts
	# Get origin package
	wget ${PACKAGE_SOURCE}/v${PACKAGE_VERSION}/pam_ssh_agent_auth-${PACKAGE_VERSION}.tar.bz2 -O ~/package.tar.bz2
	# Extract origin package
	mkdir -p ~/package
	tar xfv ~/package.tar.bz2 -C ~/package --strip-components=1
	# Build package
	cd ~/package && debuild -i -us -uc -b
	# Move package files
	rm -f /srv/files/debian_jessie/*.deb
	mv ~/*.deb /srv/files/debian_jessie

build-package@ubuntu-trusty:
	apt-get install -y wget build-essential debhelper autotools-dev libssl-dev libpam0g-dev devscripts
	# Get origin package
	wget ${PACKAGE_SOURCE}/v${PACKAGE_VERSION}/pam_ssh_agent_auth-${PACKAGE_VERSION}.tar.bz2 -O ~/package.tar.bz2
	# Extract origin package
	mkdir -p ~/package
	tar xfv ~/package.tar.bz2 -C ~/package --strip-components=1
	# Build package
	cd ~/package && debuild -i -us -uc -b
	# Move package files
	rm -f /srv/files/ubuntu_trusty/*.deb
	mv ~/*.deb /srv/files/ubuntu_trusty
