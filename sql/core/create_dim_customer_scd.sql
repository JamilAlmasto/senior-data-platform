CREATE TABLE dim_customer_scd (
    customer_sk SERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    country TEXT,
    valid_from TIMESTAMP NOT NULL,
    valid_to TIMESTAMP,
    is_current BOOLEAN NOT NULL
);

