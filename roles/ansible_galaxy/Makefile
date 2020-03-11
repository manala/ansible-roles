.SILENT:

##########
# Manala #
##########

include .manala/make/Makefile

########
# Role #
########

ROLE               = manala.ansible_galaxy
ROLE_DISTRIBUTIONS = debian.wheezy debian.jessie debian.stretch debian.buster

define docker_molecule
	docker run \
		--rm \
		--tty --interactive \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		--volume $(HOME)/.cache/molecule:/root/.cache/molecule \
		--volume $(CURDIR):/srv/$(ROLE) \
		--workdir /srv/$(ROLE) \
		manala/ansible:edge \
		$(1)
endef

define molecule
	$(call docker_molecule,molecule $(if $(DEBUG),--debug )$(1))
endef

molecule.sh:
	$(call docker_molecule,/bin/sh)

# Juste le linting
molecule.lint:
	$(call molecule,lint)

molecule.lint/%:
	$(call molecule,lint) -s $(*)

# Up
molecule.create:
	$(call molecule,create)

molecule.create/%:
	$(call molecule,create) -s $(*)

# Down
molecule.destroy:
	$(call molecule,destroy)

molecule.destroy/%:
	$(call molecule,destroy) -s $(*)

#molecule.list:
#	$(call molecule,list)

molecule.converge:
	$(call molecule,converge)

molecule.converge/%:
	$(call molecule,converge) -s $(*)

molecule.verify:
	$(call molecule,verify)

molecule.verify/%:
	$(call molecule,verify) -s $(*)

molecule.login/debian.jessie:
	$(call molecule,login --host debian.jessie)

molecule.login/debian.stretch:
	$(call molecule,login --host debian.stretch)

molecule.login/debian.buster:
	$(call molecule,login --host debian.buster)

# La totale
molecule.test:
	$(call molecule,test --all --parallel)

molecule.test/%:
	$(call molecule,test --parallel) -s $(*)
