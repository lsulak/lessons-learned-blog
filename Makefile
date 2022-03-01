# Makefile for Python development & CI
# You need: black, flake8, pylint, mdl (installable via gem).

#
# The first part of the Makefile is related (and actually, auto-generated) to Pelican.
#
SHELL := /bin/bash

PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

S3_BUCKET=lsulak-deployed-blog

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make s3_upload                      upload the web site via S3         '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif

devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

s3_upload: publish
	aws s3 sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl public-read --delete

.PHONY: html help clean regenerate serve serve-global devserver stopserver publish s3_upload


#
# The second part of the Makefile is related to Python development/CI
#
test: lint unit-tests

venv-create:
	[ -d $(BASEDIR)/.venv ] || python3 -m venv $(BASEDIR)/.venv

lint: black-ci flake8 pylint-shorter readme-lint

install:
	@echo 'Going to install Python requirements'
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo ''

	@echo 'Going to install Pelican-related dependencies'
	[ -d themes/Flex ] || git clone https://github.com/alexandrevicenzi/Flex themes/Flex
	[ -d pelican-plugins ] || git clone --recursive https://github.com/getpelican/pelican-plugins
	@echo ''

	@echo 'Going to load static content and custom settings into Pelican theme'
	cp -r flex_modified/* themes/Flex/templates

black:
	black --line-length 99 --exclude="pelican-plugins|.venv" .

black-ci:
	echo -e "\n# Diff for each file:"; \
	black --line-length 99 --exclude="pelican-plugins|.venv" --diff .; \
	echo -e "\n# Status:"; \
	black --line-length 99 --exclude="pelican-plugins|.venv" --check .

flake8:
	flake8 --extend-exclude .venv,build

PYLINT_FILES = `find . \
		-path './docs' -prune -o \
		-path './.venv' -prune -o \
		-path './build' -prune -o \
		-path './themes' -prune -o \
		-path './pelican-plugins' -prune -o \
		-name '*.py' -print`;

pylint:
	python3 -m pylint $(PYLINT_FILES)

pylint-shorter:
	python3 -m pylint --disable=bad-continuation --enable=useless-suppression $(PYLINT_FILES)

readme-lint:
	mdl README.md

unit-tests:
	echo "Unit tests are not implemented for this project"
	# python3 -m pytest -rxXs --cov

clean-all: clean
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '.pytest_cache' -type d | xargs rm -rf
	find . -name '__pycache__' -type d | xargs rm -rf
	find . -name '.coverage' -delete
	find . -name '.ipynb_checkpoints' -type d | xargs rm -rf
