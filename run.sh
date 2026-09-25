#!/usr/bin/env bash
set -e

echo "========================================================"
echo "  Starting KisanDr AI - Smart Agricultural Diagnostics"
echo "========================================================"

python3 -m pip install -r requirements.txt
python3 -m app.create_samples

echo "Launching Web Server on http://localhost:8000 ..."
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
