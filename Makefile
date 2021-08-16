.SILENT:

ANSIBLE_COLLECTION=roles
ANSIBLE_NAMESPACE=manala

##########
# Docker #
##########

define docker_run
	docker run \
		--rm \
		--tty \
		--interactive \
		--hostname ansible \
		--mount 'type=bind,source=$(CURDIR),target=/srv/ansible_collections/$(ANSIBLE_NAMESPACE)/$(ANSIBLE_COLLECTION)' \
		--mount 'type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock' \
		--workdir /srv/ansible_collections/$(ANSIBLE_NAMESPACE)/$(ANSIBLE_COLLECTION) \
		quay.io/ansible/toolset:3.5.0 \
		$(strip $(1))
endef

######
# Sh #
######

sh:
	$(call docker_run)
.PHONY: sh

########
# Lint #
########

lint:
	$(call docker_run, ansible-lint)
.PHONY: lint

########
# Test #
########

test: test.sanity test.units
.PHONY: test

test.sanity:
	$(call docker_run, ansible-test sanity --python 3.8 --requirements --verbose --color)
.PHONY: test.sanity

test.units:
	$(call docker_run, ansible-test units --python 3.8 --requirements --verbose --color)
.PHONY: test.units

############
# Molecule #
############

molecule:
	$(call docker_run, molecule test --all)
	$(call docker_run, molecule test \
		$(if $(ROLE),--scenario-name $(ROLE),--all))
.PHONY: molecule
