##########
# Colors #
##########

MANALA_COLOR_RESET   := \033[0m
MANALA_COLOR_ERROR   := \033[31m
MANALA_COLOR_INFO    := \033[32m
MANALA_COLOR_WARNING := \033[33m
MANALA_COLOR_COMMENT := \033[36m

######################
# Special Characters #
######################

# Usage:
#   $(call manala_message, Foo$(,) bar) = Foo, bar
#   $(call manala_message, $(lp)Foo bar) = (Foo bar
#   $(call manala_message, Foo$(rp) bar) = Foo) bar

, := ,
lp := (
rp := )

########
# Time #
########

# Usage:
#   $(call manala_time) = 11:06:20

define manala_time
`date -u +%T`
endef

###########
# Message #
###########

# Usage:
#   $(call manala_message, Foo bar)         = Foo bar
#   $(call manala_message_success, Foo bar) = (っ◕‿◕)っ Foo bar
#   $(call manala_message_warning, Foo bar) = ¯\_(ツ)_/¯ Foo bar
#   $(call manala_message_error, Foo bar)   = (╯°□°)╯︵ ┻━┻ Foo bar

define manala_message
	printf "$(MANALA_COLOR_INFO)$(strip $(1))$(MANALA_COLOR_RESET)\n"
endef

define manala_message_success
	printf "$(MANALA_COLOR_INFO)(っ◕‿◕)っ $(strip $(1))$(MANALA_COLOR_RESET)\n"
endef

define manala_message_warning
	printf "$(MANALA_COLOR_WARNING)¯\_(ツ)_/¯ $(strip $(1))$(MANALA_COLOR_RESET)\n"
endef

define manala_message_error
	printf "$(MANALA_COLOR_ERROR)(╯°□°)╯︵ ┻━┻ $(strip $(1))$(MANALA_COLOR_RESET)\n"
endef

#######
# Log #
#######

# Usage:
#   $(call manala_log, Foo bar)         = [11:06:20] [target] Foo bar
#   $(call manala_log_warning, Foo bar) = [11:06:20] [target] ¯\_(ツ)_/¯ Foo bar
#   $(call manala_log_error, Foo bar)   = [11:06:20] [target] (╯°□°)╯︵ ┻━┻ Foo bar

define manala_log
	printf "[$(MANALA_COLOR_COMMENT)$(call manala_time)$(MANALA_COLOR_RESET)] [$(MANALA_COLOR_COMMENT)$(@)$(MANALA_COLOR_RESET)] " ; $(call manala_message, $(1))
endef

define manala_log_warning
	printf "[$(MANALA_COLOR_COMMENT)$(call manala_time)$(MANALA_COLOR_RESET)] [$(MANALA_COLOR_COMMENT)$(@)$(MANALA_COLOR_RESET)] "  ; $(call manala_message_warning, $(1))
endef

define manala_log_error
	printf "[$(MANALA_COLOR_COMMENT)$(call manala_time)$(MANALA_COLOR_RESET)] [$(MANALA_COLOR_COMMENT)$(@)$(MANALA_COLOR_RESET)] " ;  $(call manala_message_error, $(1))
endef

###########
# Confirm #
###########

# Usage:
#   $(call manala_confirm, Foo bar) = ༼ つ ◕_◕ ༽つ Foo bar (y/N):
#   $(call manala_confirm, Bar foo, y) = ༼ つ ◕_◕ ༽つ Foo bar (Y/n):

define manala_confirm
	$(if $(CONFIRM),, \
		printf "$(MANALA_COLOR_INFO) ༼ つ ◕_◕ ༽つ $(MANALA_COLOR_WARNING)$(strip $(1)) $(MANALA_COLOR_RESET)$(MANALA_COLOR_WARNING)$(if $(filter y,$(2)),(Y/n),(y/N))$(MANALA_COLOR_RESET): " ; \
		read CONFIRM ; \
		case $$CONFIRM in $(if $(filter y,$(2)), \
			[nN]$(rp) printf "\n" ; exit 1 ;; *$(rp) ;;, \
			[yY]$(rp) ;; *$(rp) printf "\n" ; exit 1 ;; \
		) esac \
	)
endef

################
# Conditionals #
################

# Usage:
#   $(call manala_error_if_not, $(FOO), FOO has not been specified) = (╯°□°)╯︵ ┻━┻ FOO has not been specified

define manala_error_if_not
	$(if $(strip $(1)),, \
		$(call manala_message_error, $(strip $(2))) ; exit 1 \
	)
endef

# Usage:
#   $(call manala_confirm_if, $(FOO), Foo bar) = ༼ つ ◕_◕ ༽つ Foo bar (y/N):

define manala_confirm_if
	$(if $(strip $(1)), \
		$(call manala_confirm, $(strip $(2)))
	)
endef

# Usage:
#   $(call manala_confirm_if_not, $(FOO), Foo bar) = ༼ つ ◕_◕ ༽つ Foo bar (y/N):

define manala_confirm_if_not
	$(if $(strip $(1)),, \
		$(call manala_confirm, $(strip $(2)))
	)
endef

##########
# Random #
##########

# Usage:
#   $(call manala_rand, 8) = 8th56zp2

define manala_rand
`cat /dev/urandom | LC_ALL=C tr -dc 'a-z0-9' | fold -w $(strip $(1)) | head -n 1`
endef
