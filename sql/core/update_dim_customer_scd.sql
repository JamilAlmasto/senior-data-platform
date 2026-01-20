-- 1. Build stable set of changed customers
DROP TABLE IF EXISTS tmp_changed_customers;

CREATE TEMP TABLE tmp_changed_customers AS
SELECT DISTINCT
    CAST(FLOOR(CAST(s.customer_id AS NUMERIC)) AS BIGINT) AS customer_id,
    s.country
FROM stg_online_retail s
JOIN dim_customer_scd d
  ON d.customer_id = CAST(FLOOR(CAST(s.customer_id AS NUMERIC)) AS BIGINT)
 AND d.is_current = true
WHERE s.customer_id IS NOT NULL
  AND s.customer_id <> 'NaN'
  AND d.country <> s.country;

-- 2. Close old current records
UPDATE dim_customer_scd d
SET
    valid_to = CURRENT_TIMESTAMP,
    is_current = false
FROM tmp_changed_customers c
WHERE d.customer_id = c.customer_id
  AND d.is_current = true;

-- 3. Insert new current records
INSERT INTO dim_customer_scd (
    customer_id,
    country,
    valid_from,
    valid_to,
    is_current
)
SELECT
    c.customer_id,
    c.country,
    CURRENT_TIMESTAMP,
    NULL,
    true
FROM tmp_changed_customers c;

-- 4. Cleanup
DROP TABLE tmp_changed_customers;
