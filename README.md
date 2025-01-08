# TechDemo: Python Calculator

## Table of Contents
1. [Introduction](#introduction)
2. [Objective](#objective)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Usage](#usage)
5. [Tech Stack](#tech-stack)
6. [Checklist](#checklist)
7. [Testing](#testing)
8. [Continuous Delivery Workflow](#continuous-delivery-workflow)
9. [Anti Patterns](#anti-patterns)
10. [License](#license)
11. [Contact](#contact)

## Introduction
This repository serves as a guide for the TechDemo of the Continuous Delivery (CD) course.
It focuses on integrating CD principles into an existing software project rather than developing new software from scratch.
The aim is to demonstrate automated builds, tests, and deployments in a real-world scenario.

### TechDemo Topic: Python Calculator
I chose to implement a very simple python calculator for this TechDemo.
I made this decision because I do not have a lot of experience with Python but often have to use it in my day-to-day work, dealing with AI and ML models.
For following the development steps of the project a [Detailed documentation](https://github.com/SusanneJandl/continuous-delivery-techdemo/blob/main/docs/detailed_steps.md) is provided.

### Branching Strategy
As this project is done by myself as a single person, the strategy was to have a working version of the project in the `main` branch.
After the first workin version existed, new implementation was done in a new branch and merged into `main` when ready.

## Objective
The main objective is to apply CD practices by automating key processes, ensuring a smoother and more efficient software development lifecycle. This includes:
- Automated builds with build tools.
- Automated testing with unit, integration, and end-to-end tests.
- Continuous deployment to production-like environments.

## Getting Started

### Prerequisites
Ensure the following software and tools are installed:
- **Git**: Version control.
- **Python**: For application.
- **Docker**: For containerization.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SusanneJandl/continuous-delivery-techdemo.git
   ```
2. It is recommended to create a python virtual environment:
   ```bash
   python -m venv techdemo_env

   techdemo_env/Scripts/activate (Windows)

   techdemo_env/bin/activate (Linux)
   ```
3. Install dependencies:
     ```bash
     pip install -r dev-requirements.txt
     ```
   - dev-requirements includes additional packages that are not needed in production
     - for testing and building

## Usage
1. **Run the tests**:
   - Execute unit tests with `pytest` form root directory

2. **Run the application (without docker)**:
   - Run the application with `python calculator/app.py`

3. **Build the project (build docker image)**: 
   - Docker: `docker build -t my-calculator_app .`

3. **Run the project (with docker)**: 
   - Docker: `docker run -p 5000:5000 my-calculator_app`

4. **Deploy the project**: The deployment is automated through the configured CI/CD pipeline using GitHub Actions.

Alternatively you can deploy the application manually on [Render.com](https://render.com)

5. **Test the deployment**: You can test the deployment by accessing the application at the assigned URL: [https://my-calculator-app-37u3.onrender.com](https://my-calculator-app-37u3.onrender.com)

### Using invoke tasks

- created tasks.py
- following tasks are available:
  - lint: uses flake8 and black
  - test: uses pytest
  - build: builds the docker image and starts the container after lint and test

- run `invoke lint`, `invoke test`, or `invoke build`

## Tech Stack
- **Primary Language**: Python
- **Build Tools**: Docker
- **Testing Frameworks**: pytest
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Checklist
For a detailed list of tasks and goals, refer to the [Checkliste](https://git-iit.fh-joanneum.at/msd-contdel/techdemo-ws24/jandl/-/blob/main/CHECKLIST.md).
This document serves as a guide to ensure all relevant CD aspects are integrated into this demo.

## Testing

### Unit Tests
To ensure high-quality code, testing is integrated throughout the development process.
Unit tests in [tests/test_calculator.py](https://github.com/SusanneJandl/continuous-delivery-techdemo/blob/main/tests/test_calculator.py) validate the correctness of [calculator/calculator.py](https://github.com/SusanneJandl/continuous-delivery-techdemo/blob/main/calculator/calculator.py).

### Code quality with flake8 and black
- flake8 identifies and shows code parts that need improvement.
- black formats the code automatically.
- first run black on the code base with the command `black .` to format the code
- then run flake8 on the code base with the command `flake8 .` to double check the formatting
- added code quality check to workflow

## Continuous Delivery Workflow
The following CD practices are integrated into this project: on push
- **Automated Builds**: Triggered on every commit.
- **Code Quality Check**: Running flake8 and black
- **Automated Tests**: Running unit tests and creating a report
- **Update Docker image on Docker Hub**: Existing Docker image is updated
- **Continuous Deployment**: Deployments to a production environment

### Pipeline Documentation

The pipeline consists of two jobs: build_and_test and deploy_to_render.

The pipeline is triggered on push and pull request events.

The first job (build_and_test) builds the docker image and runs the tests.

Steps:
- Checkout code with actions/checkout@v4
  - [actions/checkout@v4](https://github.com/marketplace/actions/checkout):
    This action checks-out your repository under $GITHUB_WORKSPACE, so your workflow can access it.
- Set up Python with actions/setup-python@v5
  - [actions/setup-python@v5](https://github.com/marketplace/actions/setup-python):
    This action provides the installation of a version of Python or PyPy and (by default) adding it to the PATH
- Install dependencies
  - here the following commands are used: `pip install --upgrade pip` and `pip install -r dev-requirements.txt`
    - upgrade pip
    - the install the dependencies defined in the file dev-requirements.txt in the project root directory.
- Check code format with Black
  - here the following command is used: `black --check . || (echo "Black found linting errors. Run 'black' locally, check code quality with 'flake8' and 'black --check', solve the errors, and commit the changes." exit 1)`
    - if the check fails, a message is printed and then the exit code is set to 1 and the build fails.
- Lint code with Flake8
  - here the following command is used: `flake8 . || (echo "Flake8 found linting errors. Check code quality locally with 'flake8' and 'black --check', solve the errors, and commit the changes." exit 1)`
    - if the check fails, a message is printed and then the exit code is set to 1 and the build fails.
- Run tests with pytest and generate report
  - here the following command is used: `pytest --maxfail=1 --disable-warnings --junitxml=test-report.xml`
    - it defines that pytest should fail if at least 1 test fails
    - it disables warnings from pytest
    - it generates an XML report named test-report.xml
    - this command needs pytest and pytest-html installed, which is defined in dev-requirements.txt
- Upload Test Results as artifact with actions/upload-artifact@v4:
  - [actions/upload-artifact@v4](https://github.com/marketplace/actions/upload-artifact):
    stores the results of the tests in an artifact named test-results
- Log in to Docker Hub with docker/login-action@v3.3.0
  - [docker/login-action@v3.3.0](https://github.com/marketplace/actions/docker-login):    
    GitHub Action to login against a Docker registry.
    Docker credentials are stored in and retrieved from GitHub secrets.
- Build Docker Image
  - here the following command is used: `docker build -t sj-images:my-calculator-app .`
    - build docker image from dockerfile in root of repository
- Push docker image to Docker Hub
  - here the following commands are used: `docker push ${{ secrets.DOCKER_USERNAME }}/sj-images:my-calculator-app` and `sleep 30`             
    - push docker image to Docker Hub (public repository)
    - wait for 30 seconds (to make sure upload is available for next pipeline job)

The second job (deploy_to_render) deploys the docker image to Render and initializes a container.
To start this job build_and_test needs to be completed successfully.

Step:

-  Deploy to Render with gh-actions-workflows/deploy-docker-render@v1.1
   - [gh-actions-workflows/deploy-docker-render@v1.1](https://github.com/gh-actions-workflows/deploy-docker-render)
     The gh-actions-workflows/deploy-docker-render action is a JavaScript action that deploys a Docker image to an existing service on Render platform.
     Render deploy hook, docker image url and render api key are required.
     All of these are stored in and retrieved from GitHub secrets.
     With wait-for-deployment, the action will wait for the deployment to be ready before continuing the pipeline.

## Anti Patterns

- Bloated Build
  - one big workflow, including waiting time for deployment

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/SusanneJandl/continuous-delivery-techdemo/blob/main/LICENSE) file for details.

## Contact
For any inquiries or issues including CONTRIBUTION, please reach out to [susanne.jandl@edu.fh-joanneum](mailto:susanne.jandl@edu.fh-joanneum.at).
