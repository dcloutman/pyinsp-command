#!/usr/bin/env python3
"""
Unit tests for pyinsp library functions.
"""

import sys
import unittest
import json
from pathlib import Path
from unittest.mock import patch
from io import StringIO

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.pyinsp import find_python_files, collect_files, display_plain, display_json, run_inspection
from lib.linter import has_parse_errors, SyntaxErrorInfo

class TestPyinsp(unittest.TestCase):
    """Unit tests for pyinsp functions."""
    
    def setUp(self):
        """Set up paths to test data files."""
        self.data_dir = Path(__file__).parent.parent / "data"
        self.valid_file = self.data_dir / "valid_script.py"
        self.simple_error_file = self.data_dir / "simple_error.py"
        self.complex_error_file = self.data_dir / "complex_error.py"

    def test_has_parse_errors_returns_false_for_valid_python(self):
        """has_parse_errors() should return False for syntactically valid Python files."""
        result = has_parse_errors(self.valid_file)
        self.assertFalse(result)

    def test_has_parse_errors_returns_syntax_error_info_for_invalid_python(self):
        """has_parse_errors() should return SyntaxErrorInfo for files with syntax errors."""
        result = has_parse_errors(self.simple_error_file)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["file"], str(self.simple_error_file))
        self.assertIsInstance(result["line"], int)
        self.assertGreater(result["line"], 0)

    def test_find_python_files_finds_py_files_in_directory(self):
        """find_python_files() should find all .py files in the test data directory."""
        files = find_python_files(self.data_dir, recursive=False)
        py_files = [f for f in files if f.suffix == '.py']
        self.assertGreaterEqual(len(py_files), 3)  # At least our 3 test files

    def test_collect_files_returns_single_file_when_given_file_path(self):
        """collect_files() should return the file itself when given a single file path."""
        files = collect_files([str(self.valid_file)], recursive=False)
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0], self.valid_file)

    def test_collect_files_finds_py_files_when_given_directory(self):
        """collect_files() should find Python files when given a directory path."""
        files = collect_files([str(self.data_dir)], recursive=False)
        self.assertGreaterEqual(len(files), 3)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_plain_shows_ok_for_files_with_no_errors(self, mock_stdout):
        """display_plain() should show 'OK' for files with line=0 (no errors)."""
        results = [SyntaxErrorInfo(file="test1.py", line=0)]
        display_plain(results)
        self.assertIn("test1.py: OK", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_plain_shows_line_number_for_files_with_errors(self, mock_stdout):
        """display_plain() should show filename:line for files with syntax errors."""
        results = [SyntaxErrorInfo(file="test1.py", line=5)]
        display_plain(results)
        self.assertIn("test1.py:5", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_json_outputs_valid_json(self, mock_stdout):
        """display_json() should output valid JSON that can be parsed."""
        results = [SyntaxErrorInfo(file="test.py", line=5)]
        display_json(results)
        output = mock_stdout.getvalue()
        parsed = json.loads(output)
        self.assertEqual(parsed[0]["file"], "test.py")
        self.assertEqual(parsed[0]["line"], 5)

    @patch('builtins.exit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_inspection_exits_0_when_no_syntax_errors(self, mock_stdout, mock_exit):
        """run_inspection() should not call exit() when all files are valid."""
        run_inspection([str(self.valid_file)], False, False)
        mock_exit.assert_not_called()

    @patch('builtins.exit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_inspection_exits_1_when_syntax_errors_found(self, mock_stdout, mock_exit):
        """run_inspection() should call exit(1) when syntax errors are found."""
        run_inspection([str(self.simple_error_file)], False, False)
        mock_exit.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main() #pyrefly: ignore
