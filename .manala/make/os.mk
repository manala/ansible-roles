######
# Os #
######

# Os detection helpers.
#
# Examples:
#
# Example #1: conditions on linux
#
#   echo $(if $(OS_LINUX),Running on Linux,*NOT* running on Linux)

ifeq ($(OS),Windows_NT)
OS := windows
else
OS := $(shell uname | tr '[:upper:]' '[:lower:]')
endif

ifeq ($(OS),linux)
OS_LINUX := 1
endif

ifeq ($(OS),darwin)
OS_DARWIN := 1
endif

ifeq ($(OS),windows)
OS_WINDOWS := 1
endif
