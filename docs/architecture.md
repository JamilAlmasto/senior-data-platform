## Analytics Architecture

The platform follows a layered approach:

- Staging: raw cleaned data
- Core: historized dimensions (SCD Type 2) and AS-OF joins
- Marts: BI-friendly aggregated views

Business users and BI tools should only query the marts layer.

