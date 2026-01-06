# Core Business Rules – Online Retail

## Definition of a Sale
A record is considered a valid sale if:
- Quantity > 0
- UnitPrice > 0
- InvoiceNo does NOT start with 'C'

## Returns & Cancellations
- Quantity <= 0 OR InvoiceNo starting with 'C'
- Considered returns or cancellations
- Excluded from core fact tables
- Preserved in staging only

## Customer Rules
- CustomerID is mandatory in core facts
- Records without CustomerID are excluded from fact_sales
- Customer dimension is built from distinct valid CustomerIDs

