INSERT INTO dim_customer_scd (
    customer_id,
    country,
    valid_from,
    valid_to,
    is_current
)
SELECT
    customer_id,
    country,
    MIN(ingestion_ts) AS valid_from,
    NULL AS valid_to,
    TRUE AS is_current
FROM fact_sales
GROUP BY customer_id, country;

