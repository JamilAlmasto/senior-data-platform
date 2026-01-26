SELECT
    sales_date,
    country,
    COUNT(*)
FROM mart_sales_daily
GROUP BY sales_date, country
HAVING COUNT(*) > 1;
