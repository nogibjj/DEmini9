[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml)

[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/format.yml)

[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/install.yml)
[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/lint.yml)
[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/test.yml)

## Template for Python projects with RUFF linter



1. First thing to do on launch is to open a new shell and verify virtual env is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Ruff`:  

Run `make lint` which runs `ruff check`.  You can find out more info on [Ruff here](https://github.com/astral-sh/ruff).

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* A base set of libraries for devops and web

* `githubactions`

## Project Directory Structure
The structure of the project is as follows:

```text
- ./
    - repeat.sh
    - setup.sh
    - main.ipynb
    - LICENSE
    - requirements.txt
    - READMEtmp.md
    - Dockerfile
    - Makefile
    - test_lib.py
    - readme_generator.py
    - README.md
    - main.py
    - test.md
    - test_main.py
    - __pycache__/
        - calculator.cpython-312.pyc
    - mylib/
        - lib.py
        - __init__.py



