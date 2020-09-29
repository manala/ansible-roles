.SILENT:

##########
# Manala #
##########

include .manala/make/Makefile

#########
# Roles #
#########

ROLES_DEPRECATED = \
	heka \
	rtail

############
# Molecule #
############

MOLECULE_VERSION = 3.0.8

 .PHONY: molecule

molecule:
	docker run \
		--rm \
		--interactive \
		--tty \
		--env DIR=$(CURDIR) \
    --volume $(CURDIR):/srv:ro \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --workdir /srv \
    quay.io/ansible/molecule:$(MOLECULE_VERSION) \
    sh
