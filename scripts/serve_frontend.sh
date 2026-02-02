#!/bin/bash
# Frontend Server Runner
# Starts the API server to serve dashboard data

set -e  # Exit on error

cd "$(dirname "$0")/.." # Change to repo root

echo "Starting API Server..."
echo "Access at: http://localhost:8000"
echo ""

python3 api/app.py
