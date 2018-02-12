
.PHONY: test publish virtualenv

INVENV = $(shell python -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')

virtualenv:
ifeq ($(INVENV), 0)
	@echo "must run under virtualenv: \033[92msource virtualenv.sh\033[0m"
	@exit 1
endif

install: virtualenv
	pip install -r requirements.pip

test: install
	pytest tests/*.py

publish: install
	rm -rf *.egg-info
	rm -rf dist
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
