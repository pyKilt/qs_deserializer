
.PHONY: test publish

test:
	pytest tests/*.py

publish:
	rm -rf *.egg-info
	rm -rf dist
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
