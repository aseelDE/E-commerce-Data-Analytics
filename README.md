# E-commerce Data Pipeline

## Overview
An end-to-end data pipeline that ingests e-commerce data from the Fake Store API, loads it into BigQuery, transforms it into analytical tables, and visualizes it in Looker Studio.

## Architecture
Fake Store API → Python → BigQuery (Raw) → SQL Transformations → BigQuery (Analytics) → Looker Studio

## Tech Stack
- Python
- Google BigQuery
- Prefect Cloud
- Looker Studio
- GitHub

## Pipeline Steps
1. Ingest data from Fake Store API (users, products, carts)
2. Load raw data into BigQuery
3. Transform data into analytics tables
4. Visualize in Looker Studio
5. Orchestrate with Prefect Cloud

## Tables
- `ecommerce_raw` — raw ingested data
- `ecommerce_analytics.top_products` — top products by rating
- `ecommerce_analytics.user_purchase_summary` — purchases per user
- `ecommerce_analytics.cart_details` — flattened cart data with revenue