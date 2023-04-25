ACTIVATE_SCRIPT := venv/bin/activate
PYTHON := python3
ifeq ($(OS),Windows_NT)
	ACTIVATE_SCRIPT := venv/Scripts/activate
	PYTHON := python
endif

venv: venv/touchfile

venv/touchfile: requirements/development.txt
	which ${PYTHON}
	which pip3
	which virtualenv || pip3 install virtualenv
	test -d venv || virtualenv venv -p ${PYTHON}
	. ${ACTIVATE_SCRIPT} && \
	pip3 install -Ur requirements/development.txt && \
	touch venv/touchfile

.PHONY: setup
setup: venv ## Setup Python development environment
	@echo
	@echo "Please make sure to source ${ACTIVATE_SCRIPT}."
	@echo
