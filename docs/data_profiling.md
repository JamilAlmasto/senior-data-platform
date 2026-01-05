# Raw Data Profiling – Online Retail

## Dataset Overview
- Rows: ~540k
- Columns: 8

## Key Data Quality Findings
- Missing CustomerID in 135080 of rows
- Negative Quantity values 10624
- Negative price values 2
- Invoices starting with "C" indicate cancellations
- Duplicate InvoiceNo + StockCode combinations exist

## Engineering Implications
- Raw data must be preserved as-is
- Staging layer must handle missing CustomerID
- Business rules needed to separate sales vs returns
- Fact tables must decide how to treat cancellations

