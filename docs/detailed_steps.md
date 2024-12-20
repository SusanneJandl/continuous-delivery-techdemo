# Pyton calculator

## Setup expected project structure

```
my_calculator
├── .github
│   └── workflows
│       └── ci.yml        
├── docs
|   ├── img
│   └── detailed_steps.md
├── calculator
│   └── calculator.py
├── tests
│   ├── __main__.py
│   └── test_calculator.py 
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```
## Create python scripts for calculator

### calculator.py with functions
```python
class Calculator:

    """Return the sum of a and b."""
    def add(self, a: float, b: float) -> float:
        return a + b
        ...
```

### \_\_main\_\_.py as entry point
```python
from calculator.calculator import Calculator

def main():
    """Entry point of the calculator application."""
    print("\nWelcome to the Python Calculator!")
    ...
    ...
if __name__ == "__main__":
    main()
```
  - imports calculator class from calculator.py
  - is entry point when running `python -m calculator` from the command line

## Create unit tests for calculator

### prerequisites

- add pytest to requirements.txt
- create python environment with `python -m venv cd_env`
- activate python environment with `cd_env\Scripts\activate`
- install requirements with `pip install -r requirements.txt`

### test_calculator.py
```python
import pytest
from calculator.calculator import Calculator

"""Fixture to create a Calculator instance before each test."""
@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-2, 3) == 1
    ...
```

- due to the project structure tests could not find calculator.py
- added pytest.ini file in root
  ```
  [pytest]
  pythonpath = .
  ```
  