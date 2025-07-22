import sys
import json
from pathlib import Path
from typing import Sequence, List
from lib.linter import has_parse_errors, SyntaxErrorInfo

def find_python_files(directory: Path, recursive: bool) -> List[Path]:
    """Find all Python files in a directory, optionally recursively."""
    if recursive:
        return [p for p in directory.rglob('*.py') if p.is_file()]
    else:
        return [p for p in directory.glob('*.py') if p.is_file()]

def collect_files(paths: Sequence[str], recursive: bool) -> List[Path]:
    """Collect all Python files from the given paths."""
    files = []
    for path_str in paths:
        path = Path(path_str)
        if path.is_file() and path.suffix == '.py':
            files.append(path)
        elif path.is_dir():
            files.extend(find_python_files(path, recursive))
    return files

def display_plain(results: List[SyntaxErrorInfo]) -> None:
    """Display results in plain text."""
    for result in results:
        if result['line'] == 0:
            print(f"{result['file']}: OK")
        else:
            print(f"{result['file']}:{result['line']}")

def display_json(results: List[SyntaxErrorInfo]) -> None:
    """Display results in JSON format."""
    print(json.dumps(results, indent=2))

def run_inspection(paths: Sequence[str], recursive: bool, output_json: bool) -> None:
    """Orchestrate the inspection process."""
    num_errors = 0

    files: list[Path] = collect_files(paths, recursive)
    results: list[SyntaxErrorInfo] = []
    for file_to_test in files:
        test_result: bool | SyntaxErrorInfo = has_parse_errors(file_to_test)

        if test_result != False:
            # Test result should be a SyntaxErrorInfo object.
            results.append(test_result) #pyrefly: ignore
            num_errors += 1
    if output_json:
        display_json(results)
    else:
        display_plain(results)
    # Set exit_code to 1 if any file has a syntax error
    if num_errors > 0:
        exit(1)
    