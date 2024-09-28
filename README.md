[![CI](https://github.com/nogibjj/DEIndividual1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/cicd.yml)

[![Format](https://github.com/nogibjj/DEIndividual1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/DEIndividual1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/DEIndividual1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/DEIndividual1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/DEIndividual1/actions/workflows/test.yml)

## Explore the matrix of NBA players 


## Dataset
The Best NBA Players, According To RAPTOR
Ratings, updated daily, use play-by-play and player-tracking data to calculate each player’s individual plus-minus measurements and wins above replacement, which accounts for playing time
https://github.com/fivethirtyeight/data/tree/master/nba-raptor 

## Techniques Applied
Pandas, test by nbval, show up the outcome by Jupyter.

## Data Visualization

![Minutes Played](mp_distribution.png)
![Distribution of Poss](NBA_poss.png)
## Summary Statistics

[View the Document](main.pdf)

## Main points in Video
https://youtu.be/ufjxtGhLizk 
- Brief the project, Data source, main purpose

```Techniques required
- ./
    - Jupyter Notebook with: 
        - Cells that perform descriptive statistics using Polars or Panda.
        - Tested by using nbval plugin for pytest
    - Makefile with the following:
        - Run all tests (must test notebook and script and lib)
        - Formats code with Python blackLinks to an external site.
        - Lints code with RuffLinks to an external site.
        - Installs code via:  pip install -r requirements.txt
    - test_script.py to test script
    - test_lib.py to test library
    - Pinned requirements.txt
    - Gitlab Actions performs all four Makefile commands with badges for each one in the README.md
```


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

```

1. Things included are:

* `Jupyter`  `main.ipynb`  

* `Python Script`  `main.py` 

* `pandas`

* `nbval test`  `nbval_test.py`   `main.pdf`  

* `mylib/lib.py`

* `Makefile`  `Lint and Ruff`

* `Pytest` `test_main.py` `test_lib.py`

* `requirements.txt`

* `Gitlab/Github Actions`

* `Demo Video`  

[View the Document](main.pdf)