import pandas as pd
from datetime import datetime
from pipelines.db import get_connection
from pipelines.logging import setup_logger

logger = setup_logger("ingest_to_staging")

FILE_PATH = "data/raw/OnlineRetail.csv"
SOURCE_FILE = "OnlineRetail.csv"

def run():
    logger.info("Starting raw to staging ingestion")

    df = pd.read_csv(FILE_PATH)

    df["ingestion_ts"] = datetime.utcnow()
    df["source_file"] = SOURCE_FILE

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE stg_online_retail;")

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO stg_online_retail (
                invoice_no, stock_code, description,
                quantity, unit_price, invoice_date,
                customer_id, country,
                ingestion_ts, source_file
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["InvoiceNo"],
            row["StockCode"],
            row["Description"],
            row["Quantity"],
            row["UnitPrice"],
            row["InvoiceDate"],
            row["CustomerID"],
            row["Country"],
            row["ingestion_ts"],
            row["source_file"]
        ))

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Ingestion to staging completed")

if __name__ == "__main__":
    run()

