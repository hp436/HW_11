# Calculation API

This project implements a **Calculation Model** with SQLAlchemy, Pydantic validation, and an optional Factory Pattern. It includes **unit and integration tests**, and is fully containerized with Docker. CI/CD is configured with **GitHub Actions** to run tests and push the Docker image.

---

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Testing](#testing)  
- [Docker](#docker)  
- [CI/CD](#cicd)  
- [Docker Hub](#docker-hub)  

---

## Features

- SQLAlchemy model for `Calculation` with fields: `id`, `a`, `b`, `type`, `result`  
- Pydantic schemas for input validation (`CalculationCreate`) and output serialization (`CalculationRead`)  
- Optional **Factory Pattern** to handle calculation types (`Add`, `Sub`, `Multiply`, `Divide`)  
- Unit tests for schema validation and factory logic  
- Integration tests using PostgreSQL container  
- Fully containerized with Docker  
- CI/CD pipeline to run tests and push Docker image automatically  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

