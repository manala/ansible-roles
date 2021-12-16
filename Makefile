.SILENT:

ANSIBLE_COLLECTION=roles
ANSIBLE_NAMESPACE=manala
ANSIBLE_IMAGE=quay.io/ansible/toolset:3.5.0

-include \
	./.env

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
		$(ANSIBLE_IMAGE) \
		$(strip $(1))
endef

define docker_collection
	docker run \
		--rm \
		--env COLLECTION_API_TOKEN \
		--volume $(PWD):/srv/ \
		--workdir /srv/ \
		$(ANSIBLE_IMAGE) \
		$(1)
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

##############
# Collection #
##############

MANALA_COLLECTION = $(ANSIBLE_NAMESPACE)-$(ANSIBLE_COLLECTION)-*.tar.gz

define collection
	$(call docker_collection, ansible-galaxy collection $(1))
endef

collection.build:
	rm -rf $(MANALA_COLLECTION)
	$(call collection,build --force --verbose)
.PHONY: collection.build

collection.publish:
	$(call collection,publish $(MANALA_COLLECTION) --api-key $(COLLECTION_API_TOKEN))
.PHONY: collection.publish
