CREATE TABLE fact_sales AS
SELECT
    invoice_no,
    stock_code,
    quantity,
    unit_price,
    invoice_date,
    CAST(FLOOR(CAST(customer_id AS NUMERIC)) AS BIGINT) AS customer_id,
    country,
    ingestion_ts
FROM stg_online_retail
WHERE
    quantity > 0
    AND unit_price > 0
    AND invoice_no NOT LIKE 'C%'
    AND customer_id IS NOT NULL
    AND customer_id <> 'NaN';

