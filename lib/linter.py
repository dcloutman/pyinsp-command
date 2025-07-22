"""
pyinsp: Core functionality for Python syntax checking
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, TypedDict, Union
import subprocess


class SyntaxErrorInfo(TypedDict):
    """Type definition for syntax error information."""
    file: str
    line: int | None


def has_parse_errors(filepath: Path) ->  SyntaxErrorInfo | bool:
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
        line_num = getattr(e, 'lineno', 1)
        #error_msg = getattr(e, 'msg', 'Syntax error')
        
        return SyntaxErrorInfo(
            file=str(filepath),
            line=line_num
        )

