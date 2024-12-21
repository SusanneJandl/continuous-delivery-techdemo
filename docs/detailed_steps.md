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

## Create package and publish to PyPI

### create pyproject.toml in root 

```
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-calculator-app"
version = "0.1.0"
description = "A simple calculator app for learning CI/CD and packaging."
authors = [
    { name = "Susan Example", email = "susan@example.com" }
]
license = { text = "MIT" }
readme = "README.md"
dependencies = []
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
requires-python = ">=3.7"

[project.optional-dependencies]
dev = ["pytest"]
```

### build project
- activate python environment with `cd_env\Scripts\activate` if not done yet
- add twine and build to requirements.txt
- install requirements with `pip install -r requirements.txt`
- run `python -m build` in root	
  - dist directory with calculator_app-0.1.0.tar.gz and calculator_app-0.1.0.py3-none-any.whl is created

### upload to PyPI

- prerequisites
  - create account, get API key (already did it in a previous project)
  - check if the name already exists and change it if necessary
- run `twine upload dist/*` in root
- install from PyPI with `pip install my-calculator-app` to check result
- check app information with `pip show my-calculator-app`

## Containerization with Docker

### create Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . /app

CMD ["python", "-m", "calculator"]
```

### create .dockerignore file

```
__pycache__
*.pyc
.git
.venv
*.env
dist/
build/
.eggs/
```

### build docker image

- run `docker build -t my-calculator_app .` in root
  - -t gives the name to image

### initialize docker container

- run `docker run -it my-calculator_app`
  - i for interactive mode, keeps stdin open
  - t for allocating a terminal (pseudo-TTY)

### more docker commands

- `docker ps` to list running containers
- `docker ps -a` to list all containers
- `docker stop <container_id>` to stop a container
  - find container id with `docker ps`
- `docker rm <container_id>` to remove a container
  - find container id with `docker ps -a`  

## add workflow to GitHub

- create .github/workflows/ci.yml

```yaml
name: CI/CD Workflow

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
      
permissions:  # added due to permission error in mikepenz/action-junit-report@v4
  contents: read
  checks: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r dev-requirements.txt

    - name: Run tests with pytest and generate report
      run: |
        pytest --maxfail=1 --disable-warnings --junitxml=test-report.xml
          
    - name: Upload Test Results as artifact
      uses: actions/upload-artifact@v4
      with:
        name: test-results
        path: test-report.xml

    - name: Publish Test Report
      uses: mikepenz/action-junit-report@v5
      if: success() || failure()
      with:
        report_paths: '**/test-report.xml'  
    
    - name: Build Docker image
      run: |
        docker build -t my-calculator-app .
```

## upload to dockerhub via github workflow

### prerequisites

- create dockerhub account
- create dockerhub repository

### add secret to github

- go to repository's settings -> secrets and variables -> Actions
  - do not confuse personal settings and repository settings
- add the following secrets: DOCKER_USERNAME and DOCKER_PASSWORD  

### modify workflow

- remove Build Docker image
- add
```yaml
- name: Log in to Docker Hub
  uses: docker/login-action@v2
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}

- name: Build Docker Image
  run: |
    docker build -t ${{ secrets.DOCKER_USERNAME }}/sj-images:my-calculator-app .
       
- name: Push Docker Image to Docker Hub
  run: |
    docker push ${{ secrets.DOCKER_USERNAME }}/sj-images:my-calculator-app
```

- uploaded image in repository
![dockerhub image](img/img_docker_upload.png)