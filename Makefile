.SILENT:

##########
# Manala #
##########

include .manala/make/Makefile

#########
# Roles #
#########

ROLES_DEPRECATED = \
	manala.heka \
	manala.rtail \
	manala.logentries \
	manala.ngrok \
	manala.phantomjs \
	manala.phpmyadmin \
	manala.phppgadmin \
	manala.phpredisadmin \
	manala.mailhog \
	manala.mongo_express \
	manala.oauth2_proxy \
	manala.opcache_dashboard \
	manala.thumbor \
	manala.vault
