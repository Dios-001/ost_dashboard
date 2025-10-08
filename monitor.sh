#!/bin/bash
echo "==== System Health Logger Started ===="
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
echo "[$timestamp] Logging system health..."

python3 logger.py
python3 alert.py
python3 visualize.py
python3 report.py

echo "[$timestamp] Cycle complete."
