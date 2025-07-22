"""
pyinsp: A Python syntax inspector similar to PHP's `php -l` command.
"""

import sys
from pathlib import Path
from typing import List
import click


def check_file(filepath: Path, return_line_number: bool = False) -> int:
    """Check a single Python file for syntax errors.
    
    Args:
        filepath: Path to the file to check
        return_line_number: If True, return line number as exit code (with -s flag)
                          If False, print line number and return 1 (default)
    
    Returns:
        0 if valid, otherwise:
        - If return_line_number=True: line number of syntax error (with -s flag)
        - If return_line_number=False: 1 (but prints line number) (default behavior)
    """
    try:
        # Use compile() directly to get SyntaxError with line numbers
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        compile(source, str(filepath), 'exec')
        # Valid files return 0
        return 0
    except SyntaxError as e:
        line_num = getattr(e, 'lineno', 1)
        if return_line_number:
            # Return line number as exit code (with -s flag)
            return line_num
        else:
            # Print line number, return 1 (default behavior)
            print(f"{filepath}:{line_num}")
            return 1
    except Exception:
        # File read errors, encoding issues, etc.
        if not return_line_number:
            print(f"{filepath}:1")
            return 1
        else:
            return 1


def find_python_files(path: Path, recursive: bool = False) -> List[Path]:
    """Find Python files in a directory."""
    if path.is_file():
        return [path] if path.suffix == '.py' else []
    
    if not path.is_dir():
        return []
    
    if recursive:
        return sorted(path.rglob('*.py'))
    else:
        return sorted(path.glob('*.py'))


@click.command()
@click.argument('paths', nargs=-1, required=True, type=click.Path(exists=True))
@click.option('-r', '--recursive', is_flag=True, help='Recursively check directories')
@click.option('-s', '--suppress-line-number', is_flag=True, help='Suppress line number in output, exit with line number instead of 1')
def main(paths, recursive, suppress_line_number):
    """Check Python files for syntax errors.
    
    Exit codes:
    - 0: No syntax errors
    - 1: Syntax error (default)
    - Line number (e.g., 42): Syntax error on that line (when -s is used)
    """
    exit_code = 0
    
    for path_str in paths:
        path = Path(path_str)
        
        if path.is_file():
            if path.suffix != '.py':
                continue  # Skip non-Python files silently
            result = check_file(path, return_line_number=suppress_line_number)
            if result != 0:
                exit_code = result
        elif path.is_dir():
            python_files = find_python_files(path, recursive)
            for py_file in python_files:
                result = check_file(py_file, return_line_number=suppress_line_number)
                if result != 0:
                    exit_code = result
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
