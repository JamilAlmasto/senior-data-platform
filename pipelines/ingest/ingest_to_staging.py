import pandas as pd
from datetime import datetime

import psycopg2.extras

from pipelines.db import get_connection
from pipelines.logging import setup_logger

logger = setup_logger("ingest_to_staging")

FILE_PATH = "data/raw/OnlineRetail.csv"
SOURCE_FILE = "OnlineRetail.csv"


def run() -> None:
    logger.info("Starting raw to staging ingestion")

    # 1. Read raw CSV with correct encoding
    df = pd.read_csv(FILE_PATH, encoding="latin1")

    # 2. Force object dtype (NOT pandas string dtype)
    df["CustomerID"] = df["CustomerID"].astype(object)

    # 3. Replace all pandas NA/NaN with Python None
    df = df.applymap(lambda x: None if pd.isna(x) else x)

    # 4. Add technical metadata
    ingestion_ts = datetime.utcnow()
    df["ingestion_ts"] = ingestion_ts
    df["source_file"] = SOURCE_FILE

    # 5. Select and order columns for staging
    df = df[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "InvoiceDate",
            "CustomerID",
            "Country",
            "ingestion_ts",
            "source_file",
        ]
    ]

    # 6. Convert to pure Python tuples
    records = list(df.itertuples(index=False, name=None))

    insert_sql = """
        INSERT INTO stg_online_retail (
            invoice_no,
            stock_code,
            description,
            quantity,
            unit_price,
            invoice_date,
            customer_id,
            country,
            ingestion_ts,
            source_file
        )
        VALUES %s
    """

    conn = get_connection()
    cur = conn.cursor()

    try:
        # 7. Idempotency
        cur.execute("TRUNCATE TABLE stg_online_retail;")

        # 8. Bulk insert (robust)
        psycopg2.extras.execute_values(
            cur,
            insert_sql,
            records,
            page_size=10_000,
        )

        conn.commit()
        logger.info(
            "Ingestion to staging completed successfully (rows=%s)",
            len(records),
        )

    except Exception:
        conn.rollback()
        logger.exception("Staging ingestion failed")
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    run()
