# pyinsp

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A fast, shell-friendly Python syntax inspector inspired by PHP's `php -l`.

## Features

- Simple CLI with minimal output
- Checks files and directories for Python syntax errors
- Recursive directory scanning
- Shell-friendly exit codes

## Install

```bash
pipx install pyinsp
# or
pip install pyinsp
```

## Usage

General usage:

```bash
pyinsp [OPTIONS] PATHS...
```

- `PATHS...`: One or more files or directories to check (must exist).

### Options

- `-r`, `--recursive`: Recursively check directories
- `-j`, `--output-json`: Output results in JSON format (useful for files with many lines)

### Exit Codes

- `0`: No syntax errors found
- `1`: Syntax error found 

### Examples

```bash
pyinsp script.py                 # Check a single Python file
pyinsp file1.py file2.py         # Check multiple Python files
pyinsp -r src/                   # Check all .py files in src/ recursively
pyinsp -j script.py              # Output results in JSON format
pyinsp -r -j src/                # Recursive scan with JSON output
```


## Developer Setup

### Typical Installation & Build

```bash
# Clone the repository
git clone https://github.com/dcloutman/pyinsp-command.git
cd pyinsp-command

# Create a virtual environment. `virtaulenv` can be installed locally via `pip install --user virtualenv`
virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -e .
pip install -r requirements.txt  # if requirements.txt exists
```

### Building the Project

To build the project, run the following command from the repository root:

```bash
python setup.py build
```

This will compile any necessary files and prepare the package for installation or distribution.

### Running Tests

```bash
# Run all unit and functional tests
./tests/run_tests.sh
```

Or run unit tests directly:

```bash
venv/bin/python -m unittest discover -s tests/unit
```

### Formatting & Linting
This project does not currently enforce any specific formatting or linting standards.

## License

MIT License (c) 2025 David Cloutman

v0.0.1
