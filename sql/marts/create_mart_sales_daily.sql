CREATE OR REPLACE VIEW mart_sales_daily AS
SELECT
    DATE(invoice_date) AS sales_date,
    country,
    SUM(quantity * unit_price) AS total_revenue,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT invoice_no) AS total_orders
FROM fact_sales_enriched
GROUP BY
    DATE(invoice_date),
    country;
