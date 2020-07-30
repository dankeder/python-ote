requirements.txt: requirements.in
	pip-compile --upgrade $^ --output-file $@

build:
	python3 setup.py sdist bdist_wheel

upload: build
	python3 -m twine upload dist/*

clean:
	python3 setup.py clean
	rm -rf ./dist/ ./python_ote.egg-info/ ./build/

.PHONY: build upload clean
