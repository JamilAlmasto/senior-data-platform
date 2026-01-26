import subprocess
import sys
from pipelines.logging import setup_logger

logger = setup_logger("pipeline")


def run_step(name, command):
    logger.info(f"Starting step: {name}")

    result = subprocess.run(
        command,
        shell=True
    )

    if result.returncode != 0:
        logger.error(f"Step FAILED: {name}")
        sys.exit(1)

    logger.info(f"Step PASSED: {name}")


def main():
    run_step(
        "Ingest raw to staging",
        "python -m pipelines.ingest.ingest_to_staging"
    )

    run_step(
        "Build core layer",
        "docker exec -i data_platform_postgres "
        "psql -U admin -d platform_db "
        "< sql/core/create_fact_sales_enriched.sql"
    )

    run_step(
        "Build marts",
        "docker exec -i data_platform_postgres "
        "psql -U admin -d platform_db "
        "< sql/marts/create_mart_sales_daily.sql"
    )

    run_step(
        "Run data quality checks",
        "python -m pipelines.quality.run_quality_checks"
    )

    logger.info("PIPELINE COMPLETED SUCCESSFULLY")
    sys.exit(0)


if __name__ == "__main__":
    main()
