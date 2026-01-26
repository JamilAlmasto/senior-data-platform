import sys
from pipelines.db import get_connection
from pipelines.logging import setup_logger

logger = setup_logger("quality_checks")

QUALITY_CHECKS = [
    {
        "name": "negative_revenue",
        "sql": """
            SELECT 1
            FROM mart_sales_daily
            WHERE total_revenue <= 0
            LIMIT 1;
        """
    },
    {
        "name": "null_values",
        "sql": """
            SELECT 1
            FROM mart_sales_daily
            WHERE
                sales_date IS NULL
             OR country IS NULL
             OR total_revenue IS NULL
            LIMIT 1;
        """
    },
    {
        "name": "duplicate_keys",
        "sql": """
            SELECT 1
            FROM mart_sales_daily
            GROUP BY sales_date, country
            HAVING COUNT(*) > 1
            LIMIT 1;
        """
    }
]


def run():
    conn = get_connection()
    cur = conn.cursor()

    logger.info("Starting data quality checks")

    for check in QUALITY_CHECKS:
        logger.info(f"Running check: {check['name']}")
        cur.execute(check["sql"])
        result = cur.fetchone()

        if result:
            logger.error(f"Quality check FAILED: {check['name']}")
            conn.close()
            sys.exit(1)

    logger.info("All data quality checks PASSED")
    conn.close()
    sys.exit(0)


if __name__ == "__main__":
    run()
