#!/bin/bash
# Simple shell script showing integration with pyinsp

echo "Python Syntax Checker Example"
echo "=============================="

# Check if pyinsp is available
if ! command -v pyinsp &> /dev/null; then
    echo "Error: pyinsp is not installed or not in PATH"
    exit 1
fi

echo "Checking test data files..."
pyinsp tests/data/

exit_code=$?
echo "Exit code: $exit_code"
exit $exit_code
