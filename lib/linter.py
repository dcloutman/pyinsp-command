import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, TypedDict, Union
import subprocess
from warnings import warn

"""
pyinsp: Core functionality for Python syntax checking
"""

class SyntaxErrorInfo(TypedDict):
    """Type definition for syntax error information."""
    file: str
    line: int
    level: str

def has_parse_errors(filepath: Path, include_warnings: bool = False) -> SyntaxErrorInfo | bool:
    """Check a single Python file for syntax errors.
    
    Args:
        filepath: Path to the file to check
     Returns:
        false if valid, otherwise a populated SyntaxErrorInfo object with error details.
    """
    try:
        # Use compile() directly to get SyntaxError with line numbers
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        compile(source, str(filepath), 'exec')
        return False  # No syntax errors    
    except SyntaxError as e:
        line_num = getattr(e, 'lineno', 0)
        return SyntaxErrorInfo(
            file=str(filepath),
            line=line_num,
            level="error"
        )
    except SyntaxWarning as w:
        if include_warnings:
            line_num = getattr(w, 'lineno', 0)
            return SyntaxErrorInfo(
                file=str(filepath),
                line=line_num,
                level="warning"
            )
        else:
            return False
    except Exception as ex:
        raise ex