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
9. [License](#license)
10. [Contact](#contact)

## Introduction
This repository serves as a guide for the TechDemo of the Continuous Delivery (CD) course.
It focuses on integrating CD principles into an existing software project rather than developing new software from scratch.
The aim is to demonstrate automated builds, tests, and deployments in a real-world scenario.

### TechDemo Topic: Python Calculator
I chose to implement a very simple python calculator for this TechDemo.
I made this decision because I do not have a lot of experience with Python but often have to use it in my day-to-day work, dealing with AI and ML models.
For following the development steps of the project a [Detailed documentation](https://github.com/SusanneJandl/continuous-delivery-techdemo/blob/main/docs/detailed_steps.md) is provided.

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
To ensure high-quality code, testing is integrated throughout the development process. You can run the following test suites:
1. **Unit Tests**: Validating individual components.

## Continuous Delivery Workflow
The following CD practices are integrated into this project: on push
- **Automated Builds**: Triggered on every commit.
- **Automated Tests**: Running unit tests and creating a report
- **Update Docker image on Docker Hub**: Existing Docker image is updated
- **Continuous Deployment**: Deployments to a production environment

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/SusanneJandl/continuous-delivery-techdemo/blob/main/LICENSE) file for details.

## Contact
For any inquiries or issues including CONTRIBUTION, please reach out to [susanne.jandl@edu.fh-joanneum](mailto:susanne.jandl@edu.fh-joanneum.at).
