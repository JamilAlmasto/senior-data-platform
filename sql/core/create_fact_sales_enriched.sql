CREATE OR REPLACE VIEW fact_sales_enriched AS
SELECT
    f.invoice_no,
    f.stock_code,
    f.quantity,
    f.unit_price,
    f.invoice_date,
    f.customer_id,
    d.customer_sk,
    d.country,
    f.ingestion_ts
FROM fact_sales f
JOIN dim_customer_scd d
  ON f.customer_id = d.customer_id
 AND f.invoice_date >= d.valid_from
 AND f.invoice_date < COALESCE(d.valid_to, '9999-12-31');

