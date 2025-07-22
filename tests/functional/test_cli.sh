#!/usr/bin/env bash
# Functional test for pyinsp

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
ROOT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
TEST_DATA="$ROOT_DIR/tests/data"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Run a test and check the exit code
run_test() {
    local test_name="$1"
    local cmd="$2"
    local expected_exit="$3"
    
    echo "Running test: $test_name"
    
    # Run command
    eval "$cmd" > /dev/null
    local actual_exit=$?
    
    # Check result
    if [ "$actual_exit" -eq "$expected_exit" ]; then
        echo -e "${GREEN}PASS${NC}: Exit code $actual_exit matches expected $expected_exit"
        return 0
    else
        echo -e "${RED}FAIL${NC}: Exit code $actual_exit does not match expected $expected_exit"
        return 1
    fi
}

# Track failures
failures=0

# Test 1: Valid file should exit with 0
run_test "Valid file" "$ROOT_DIR/venv/bin/python $ROOT_DIR/bin/pyinsp.py $TEST_DATA/valid_script.py" 0
failures=$((failures + $?))

# Test 2: Simple error file should exit with 1
run_test "Simple error file" "$ROOT_DIR/venv/bin/python $ROOT_DIR/bin/pyinsp.py $TEST_DATA/simple_error.py" 1
failures=$((failures + $?))

# Test 3: Complex error file should exit with 1
run_test "Complex error file" "$ROOT_DIR/venv/bin/python $ROOT_DIR/bin/pyinsp.py $TEST_DATA/complex_error.py" 1
failures=$((failures + $?))

# Test 4: Directory scan should exit with 1 (has error files)
run_test "Directory scan" "$ROOT_DIR/venv/bin/python $ROOT_DIR/bin/pyinsp.py $TEST_DATA" 1
failures=$((failures + $?))

# Test 5: Recursive directory scan
run_test "Recursive directory scan" "$ROOT_DIR/venv/bin/python $ROOT_DIR/bin/pyinsp.py -r $TEST_DATA" 1
failures=$((failures + $?))

# Test 6: JSON output format
echo "Running test: JSON output format"
output=$($ROOT_DIR/venv/bin/python $ROOT_DIR/bin/pyinsp.py -j $TEST_DATA/simple_error.py 2>/dev/null)
if echo "$output" | python -m json.tool > /dev/null 2>&1; then
    echo -e "${GREEN}PASS${NC}: JSON output is valid"
else
    echo -e "${RED}FAIL${NC}: JSON output is invalid"
    failures=$((failures + 1))
fi

# Final results
echo ""
echo "=== TEST SUMMARY ==="
if [ $failures -eq 0 ]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}$failures test(s) failed.${NC}"
    exit 1
fi
