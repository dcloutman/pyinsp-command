#!/usr/bin/env python3
"""
pyinsp: CLI for Python syntax checking
"""

import sys
import json
from pathlib import Path
import click

# Add the parent directory to the path so we can import the lib module
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.pyinsp import run_inspection


@click.command()
@click.argument('paths', nargs=-1, required=True, type=click.Path(exists=True))
@click.option('-r', '--recursive', is_flag=True, help='Recursively check directories')
@click.option('-w', '--show-warnings', is_flag=True, help='Show syntax warnings')
@click.option('-j', '--output-json', is_flag=True, help='Output results in JSON format (useful for files with many lines)')
def main(paths, recursive, output_json, show_warnings):
    """Check Python files for syntax errors.

    Exit codes:
    - 0: No syntax errors
    - 1: Syntax error

    JSON output is provided for machine-readable results.
    """
    exit_code = run_inspection(paths, recursive, output_json, show_warnings)
    sys.exit(exit_code)

if __name__ == '__main__':
    print(f"Running pyinsp from: {__file__}", file=sys.stderr)
    main()
