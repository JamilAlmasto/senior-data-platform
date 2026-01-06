CREATE TABLE dim_customer AS
SELECT DISTINCT
    CAST(FLOOR(CAST(customer_id AS NUMERIC)) AS BIGINT) AS customer_id,
    country
FROM stg_online_retail
WHERE
    customer_id IS NOT NULL
    AND customer_id <> 'NaN';

