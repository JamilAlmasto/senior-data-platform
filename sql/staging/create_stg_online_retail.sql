CREATE TABLE IF NOT EXISTS stg_online_retail (
    invoice_no      TEXT,
    stock_code      TEXT,
    description     TEXT,
    quantity        INTEGER,
    unit_price      NUMERIC(10, 2),
    invoice_date    TIMESTAMP,
    customer_id     BIGINT,
    country         TEXT,
    ingestion_ts    TIMESTAMP NOT NULL,
    source_file     TEXT NOT NULL
);

