-- 1. Close current records where attribute has changed
UPDATE dim_customer_scd d
SET
    valid_to = CURRENT_TIMESTAMP,
    is_current = FALSE
FROM (
    SELECT DISTINCT
        CAST(FLOOR(CAST(customer_id AS NUMERIC)) AS BIGINT) AS customer_id,
        country
    FROM stg_online_retail
    WHERE customer_id IS NOT NULL
      AND customer_id <> 'NaN'
) s
WHERE d.customer_id = s.customer_id
  AND d.is_current = TRUE
  AND d.country <> s.country;


-- 2. Insert new records for changed customers
INSERT INTO dim_customer_scd (
    customer_id,
    country,
    valid_from,
    valid_to,
    is_current
)
SELECT
    CAST(FLOOR(CAST(customer_id AS NUMERIC)) AS BIGINT) AS customer_id,
    country,
    CURRENT_TIMESTAMP AS valid_from,
    NULL AS valid_to,
    TRUE AS is_current
FROM (
    SELECT DISTINCT
        customer_id,
        country
    FROM stg_online_retail
    WHERE customer_id IS NOT NULL
      AND customer_id <> 'NaN'
) s
WHERE NOT EXISTS (
    SELECT 1
    FROM dim_customer_scd d
    WHERE d.customer_id = CAST(FLOOR(CAST(s.customer_id AS NUMERIC)) AS BIGINT)
      AND d.country = s.country
      AND d.is_current = TRUE
);
