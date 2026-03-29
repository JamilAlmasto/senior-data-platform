# Senior Data Platform

Production-inspired data platform demonstrating senior-level data engineering practices: ingestion, modeling, quality, history, orchestration, and analytics.

---

## Overview

This project simulates a modern data platform with a focus on best practices used in real-world data engineering.

It includes:

* Data ingestion from raw sources
* Transformation into staging and core models
* Slowly Changing Dimensions (SCD Type 2)
* Data quality checks
* Analytical data marts
* Pipeline orchestration

---

## Architecture

The platform follows a layered data architecture:

* **Raw** → Source data
* **Staging** → Cleaned and standardized data
* **Core** → Business logic and dimensional models
* **Marts** → Analytics-ready tables
* **Quality** → Data validation checks

---

## Tech Stack

* Python
* PostgreSQL
* SQL
* Environment variables for configuration

---

## Project Structure

```
pipelines/        # Pipeline orchestration and execution
sql/
  core/           # Core data models (dimensions, facts)
  marts/          # Analytical data marts
  quality/        # Data quality checks
docs/             # Architecture and documentation
tests/            # Tests (expandable)
data/             # Raw data sources
```

---

## Configuration

The pipeline is configured using environment variables.

Create a `.env` file based on the example below:

```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=platform_db
DB_USER=admin
DB_PASSWORD=admin
```


---

## How to Run

Run the full pipeline:

```bash
python pipelines/run_pipeline.py
```

Run data quality checks:

```bash
python pipelines/quality/run_quality_checks.py
```

---

##  Testing

Tests can be added in the `tests/` directory.

Example:

```python
def test_pipeline_runs():
    assert True
```

---

## Features

* SCD Type 2 implementation for customer dimension
* Modular SQL transformations
* Data quality validation checks
* Clear separation of pipeline layers
* Production-inspired project structure

---

##  Notes

This project is intended for learning and portfolio purposes, showcasing practical data engineering skills and architecture patterns.

---


