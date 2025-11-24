# HW_11 Reflection Document

## Overview

This assignment focused on creating a **Calculation model** using SQLAlchemy, validating data with Pydantic schemas, implementing an optional **Factory Pattern**, and reinforcing a **CI/CD pipeline** with Docker and GitHub Actions.  

The main goal was to strengthen skills in **Python web applications, database integration, testing, and containerization**.

---

## Key Learning Points

1. **SQLAlchemy Models**
   - Learned how to define models with fields (`id`, `a`, `b`, `type`, `result`) and optional foreign keys.
   - Explored on-demand vs stored calculation results.

2. **Pydantic Validation**
   - Implemented `CalculationCreate` and `CalculationRead` schemas.
   - Added validations such as zero-division prevention and correct operation type enforcement.

3. **Factory Pattern (Optional)**
   - Created a factory to dynamically select the correct calculation operation (`Add`, `Sub`, `Multiply`, `Divide`).
   - Improved code extensibility and separation of concerns.

4. **Unit and Integration Testing**
   - Wrote unit tests for each operation type and schema validation.
   - Integration tests used a PostgreSQL container to ensure database operations worked correctly.

5. **CI/CD and Docker**
   - Built a Docker image for the app.
   - Configured GitHub Actions to run tests and push Docker images to Docker Hub automatically.
   - Learned to troubleshoot Docker daemon issues and ASGI import errors.

---

## Challenges Faced

1. **Docker Issues**
   - Initial errors connecting to the Docker daemon.
   - ASGI app could not import `app.main` due to missing files in the Docker image.
   - Resolved by ensuring the FastAPI app and all dependencies were correctly included in the Docker build context.

2. **GitHub Repository Setup**
   - Confusion with multiple GitHub accounts (`hv2915` vs `hp436`).
   - Resolved by creating the `HW_11` repository under the correct account and updating the remote URL.

3. **Personal Access Token (PAT)**
   - Needed to push to GitHub because password authentication over HTTPS is no longer supported.
   - Learned how to generate and use a PAT for Git operations.

---

## Reflections

- This assignment strengthened understanding of **Python data modeling, API design, testing, and containerization**.
- I gained hands-on experience with **CI/CD pipelines** and how to integrate Docker with GitHub Actions.
- Using a factory pattern improved code flexibility and maintainability.
- Troubleshooting Docker and Git issues highlighted the importance of **correct environment setup** and **version control practices**.

---

## Conclusion

Overall, HW_11 helped me combine **database modeling, validation, testing, and deployment** into a cohesive workflow, simulating real-world software development practices. The experience will be valuable for future modules and real-world projects.

