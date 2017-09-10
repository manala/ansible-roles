###############
# List - Loop #
###############

MANALA_LIST_LOOP_HOOK_START_TRAVIS_FOLD = $(if $(TRAVIS), \
	MANALA_TRAVIS_FOLD=`echo $${MANALA_LIST_LOOP_ITEM} | sed -E 's/[^-_A-Za-z0-9]+/./g'` ; \
	printf "travis_fold:start:$${MANALA_TRAVIS_FOLD}\n" ; \
	MANALA_TRAVIS_TIME_ID=$(call rand) ; \
	MANALA_TRAVIS_TIME_START=$(call date_nano) ; \
	printf "travis_time:start:$${MANALA_TRAVIS_TIME_ID}\n" ; \
)

MANALA_LIST_LOOP_HOOK_END_TRAVIS_FOLD = $(if $(TRAVIS), \
	MANALA_TRAVIS_TIME_FINISH=$(call date_nano) ; \
	printf "travis_time:end:$${MANALA_TRAVIS_TIME_ID}:start=$${MANALA_TRAVIS_TIME_START}$(,)finish=$${MANALA_TRAVIS_TIME_FINISH}$(,)duration=$$(($${MANALA_TRAVIS_TIME_FINISH}-$${MANALA_TRAVIS_TIME_START}))\n" ; \
	if [ $${MANALA_LIST_LOOP_ITEM_EXIT} -eq 0 ]; then \
		printf "travis_fold:end:$${MANALA_TRAVIS_FOLD}\n" ; \
	fi ; \
)
