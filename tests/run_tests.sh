#!/bin/bash
# Run both unit and functional tests

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "=== Running Python Inspector Tests ==="
echo ""

# Run unit tests
echo "Running unit tests..."
$ROOT_DIR/venv/bin/python -m unittest discover -s $SCRIPT_DIR/unit -v
UNIT_RESULT=$?

echo ""

# Run functional tests
echo "Running functional tests..."
$SCRIPT_DIR/functional/test_cli.sh
FUNC_RESULT=$?

echo ""
echo "=== Test Results ==="
if [ $UNIT_RESULT -eq 0 ]; then
  echo -e "${GREEN}Unit tests: PASSED${NC}"
else
  echo -e "${RED}Unit tests: FAILED${NC}"
  echo "To debug unit test failures, run:"
  echo "  $ROOT_DIR/venv/bin/python -m unittest discover -s $SCRIPT_DIR/unit -v"
fi

if [ $FUNC_RESULT -eq 0 ]; then
  echo -e "${GREEN}Functional tests: PASSED${NC}"
else
  echo -e "${RED}Functional tests: FAILED${NC}"
fi

# Overall result
if [ $UNIT_RESULT -eq 0 ] && [ $FUNC_RESULT -eq 0 ]; then
  echo -e "${GREEN}All tests PASSED!${NC}"
  exit 0
else
  echo -e "${RED}Some tests FAILED!${NC}"
  exit 1
fi
