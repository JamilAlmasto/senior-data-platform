# Staging Layer Design – Online Retail

## Purpose
The staging layer preserves raw data while enforcing schema and technical metadata.

## Key Design Decisions
- No business rules applied
- Negative quantities preserved (returns)
- Missing customer IDs allowed
- Idempotent ingestion via TRUNCATE
- ingestion_ts and source_file added for traceability

## Rationale
Staging acts as a controlled landing zone, enabling reproducible transformations
and safe reprocessing without touching raw data.

