PYTHON ?= python
PYB ?= pyb

.DEFAULT_GOAL := all
.PHONY: all clean install install_deps test lint build package

all:
	$(MAKE) clean
	$(MAKE) install_deps
	$(MAKE) build

install: install_deps

install_deps:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYB) run_unit_tests

lint:
	$(PYB) analyze

build:
	$(PYB) analyze publish

package: build

clean:
	$(PYB) clean
