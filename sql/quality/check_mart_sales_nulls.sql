SELECT *
FROM mart_sales_daily
WHERE
    sales_date IS NULL
 OR country IS NULL
 OR total_revenue IS NULL;
