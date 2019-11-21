########
# Host #
########

MANALA_HOST ?= local

# Usage:
#   target: .fail_if_host_not(local)
#   	# Do something on local host...

.fail_if_host_not(%):
	$(call fail_if_host_not,$(*))

define fail_if_host_not
$(call if_eq,$(1),$(MANALA_HOST),,$(call message_error,Must be run on \"$(1)\" host); exit 1)
endef

# Usage:
#   $(call if_host,local,Yes,No) = Yes

define if_host
$(call if_eq,$(1),$(MANALA_HOST),$(2),$(3))
endef

.host_switch(%):
	$(call host_switch,$(*))

# Usage:
#   $(call host_switch,target) => make target@[host]

define host_switch
$(MAKE) $(1)@$(MANALA_HOST)
endef
