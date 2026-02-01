CREATE TABLE IF NOT EXISTS stg_online_retail (
    invoice_no TEXT,
    stock_code TEXT,
    description TEXT,
    quantity NUMERIC,
    invoice_date TIMESTAMP,
    unit_price NUMERIC,
    customer_id TEXT,
    country TEXT,
    source_file TEXT,
    ingestion_ts TIMESTAMP DEFAULT now()
);
