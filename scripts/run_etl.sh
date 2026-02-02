#!/bin/bash
# ETL Pipeline Runner
# Parses XML SMS data and generates JSON transactions

set -e  # Exit on error

cd "$(dirname "$0")/.." # Change to repo root

echo "Running ETL Pipeline..."
python3 etl/run.py

echo ""
echo "✓ ETL completed successfully"
echo "Output: data/transactions.json"
