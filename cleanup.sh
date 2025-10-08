#!/bin/bash
find logs/ -type f -name "*.txt" -mtime +7 -exec rm {} \;
echo "Old log files removed."
