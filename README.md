# Lab 6: Automatic Build with PyBuilder and Make

**Natalio Hassoun — EECE 435L, Software Tools Lab**

This lab automates a Python calculator's dependency installation, unit tests,
code checks, and packaging with PyBuilder. The optional Makefile provides short
commands for the same workflow.

## Project structure

```text
Lab6_Natalio_Hassoun/
├── README.md
├── evidence/
└── calculator_Natalio_Hassoun/
    ├── build.py
    ├── requirements.txt
    ├── Makefile
    ├── .flake8
    ├── src/main/python/calculator_Natalio_Hassoun/__init__.py
    └── tests/
        ├── __init__.py
        └── unittest/
            ├── __init__.py
            └── calculator_Natalio_Hassoun/
                ├── __init__.py
                └── test_calculator_Natalio_Hassoun.py
```

## Setup

Use Python 3.10 or newer. From the repository root:

```sh
cd calculator_Natalio_Hassoun
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```sh
source .venv/bin/activate
```

Install the build tools:

```sh
python -m pip install -r requirements.txt
```

## Exercise 1: Calculator and PyBuilder

The package implements `add`, `subtract`, `multiply`, `divide`, `modulus`,
`power`, and `square_root`. Division and modulus reject a zero divisor with
`ValueError`. Square root rejects negative real inputs with `ValueError`.
Modulus and exponentiation follow Python's `%` and `**` behavior.

Run the lab's required test command from `calculator_Natalio_Hassoun`:

```sh
pyb run_unit_tests
```

Run the complete build, including unit tests, lint checks, source distribution,
and wheel generation:

```sh
pyb clean analyze publish
```

The default tasks are `analyze` and `publish`, so `pyb` also checks and builds the
project. PyBuilder copies
the calculator sources into `target/dist/`, executes the tests, and packages the
result there. It manages its own build dependencies in `.pybuilder/`.

Run the same tests directly through Python without PyBuilder:

```sh
python -m unittest tests.unittest.calculator_Natalio_Hassoun.test_calculator_Natalio_Hassoun -v
```

The test module adds `src/main/python` to its import path so this command works
from a fresh checkout without installing the calculator first.

### Build configuration

- `python.core` copies Python source files into the build directory.
- `python.unittest` discovers `test_*.py` in the lab's `tests/unittest` tree.
- `python.install_dependencies` installs build dependencies automatically.
- `python.flake8` checks source and test style and fails on violations.
- `python.distutils` generates packaging metadata and builds an sdist and wheel.

The package uses Python's required `__init__.py` filename. Project metadata and
the default task are module-level variables in `build.py`.

## Exercise 2: Optional Makefile automation

GNU Make must be installed and available as `make`. Activate the Python
environment before using these commands:

| Command | Purpose |
| --- | --- |
| `make install` or `make install_deps` | Install the pinned build tools. |
| `make test` | Run the unit tests through PyBuilder. |
| `make lint` | Check Python style through PyBuilder. |
| `make build` or `make package` | Test, check, and package the calculator. |
| `make clean` | Remove PyBuilder's generated target directory. |
| `make all` | Clean, install dependencies, then run the full build. |

`make all` performs its steps in order, including when invoked with `make -j`.
Use `make PYTHON=python3 all` if the Python command on your machine is `python3`.

The Makefile gives repeatable names to common tasks and delegates their details
to PyBuilder. This avoids retyping long commands and keeps testing and packaging
consistent. Its cleanup uses PyBuilder instead of operating-system-specific
shell deletion commands.

## Submission evidence

The `evidence/` directory contains captured build output. To capture the terminal
screenshot requested by the handout, run `pyb run_unit_tests` inside
`calculator_Natalio_Hassoun` and include the project base directory, `BUILD
SUCCESSFUL`, build-finished timestamp, and elapsed time in the screenshot.

## References

- Lab 6 handout: *Automatic Build using PyBuilder and Make file*.
- [PyBuilder tutorial](https://pybuilder.io/documentation/tutorial)
- [PyBuilder plugin reference](https://pybuilder.io/documentation/plugins)
