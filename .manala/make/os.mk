######
# Os #
######

# Os detection helpers.
#
# Examples:
#
# Example #1: conditions on linux
#
#   echo $(if $(MANALA_OS_LINUX),Running on Linux,*NOT* running on Linux)

ifeq ($(OS),Windows_NT)
MANALA_OS = windows
MANALA_OS_WINDOWS = 1
else
# See: https://make.mad-scientist.net/deferred-simple-variable-expansion/
MANALA_OS = $(eval MANALA_OS := $$(shell uname -s | tr '[:upper:]' '[:lower:]'))$(MANALA_OS)
MANALA_OS_LINUX = $(if $(findstring linux,$(MANALA_OS)),1)
MANALA_OS_DARWIN = $(if $(findstring darwin,$(MANALA_OS)),1)
endif
