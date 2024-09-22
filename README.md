[![CI](https://github.com/nogibjj/DEIndividual1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/cicd.yml)

[![Format](https://github.com/nogibjj/DEIndividual1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/DEIndividual1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/DEIndividual1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/DEIndividual1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/test.yml)

## Explore the matrix of NBA players 


1. First thing to do on launch is to open a new shell and verify virtual env is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Ruff`:  

Run `make lint` which runs `ruff check`.  You can find out more info on [Ruff here](https://github.com/astral-sh/ruff).

* `Dockerfile`

* `jupyter`  `ipython` 

*  `nbval-test`  `.pdf` 

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
    - README.md
    - nbval_test.py
    - main.py
    - test_main.py
    - nbval_results.md
    - __pycache__/
        - calculator.cpython-312.pyc
    - generator/
        - test_generator.py
        - readme_generator.py
    - mylib/
        - lib.py
        - __init__.py
        - __pycache__/
            - test_lib.cpython-311.pyc
            - test_lib.cpython-312.pyc
            - __init__.cpython-312.pyc
            - lib.cpython-311.pyc
            - __init__.cpython-311.pyc
            - lib.cpython-312.pyc
```



