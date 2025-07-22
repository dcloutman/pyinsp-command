#!/usr/bin/env python3
"""
This is a complex test file with a syntax error in a non-trivial position.
The error is not on the first line to better test the line number reporting.
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Union, Any


class ComplexExample:
    """A complex class to demonstrate non-trivial code with a syntax error."""
    
    def __init__(self, name: str, values: List[int]):
        self.name = name
        self.values = values
        self.processed = {}
    
    def process_values(self) -> Dict[str, Any]:
        """Process the values with different operations."""
        result = {
            "sum": sum(self.values),
            "average": sum(self.values) / len(self.values) if self.values else 0,
            "min": min(self.values) if self.values else None,
            "max": max(self.values) if self.values else None,
        }
        
        # Calculate squares and cubes
        squares = [x**2 for x in self.values]
        cubes = [x**3 for x in self.values]
        
        # This line has an error - missing closing parenthesis
        if any(x > 100 for x in squares:
            result["has_large_square"] = True
        
        result["squares"] = squares
        result["cubes"] = cubes
        
        self.processed = result
        return result
    
    def save_to_json(self, filepath: Path) -> bool:
        """Save processed results to a JSON file."""
        if not self.processed:
            self.process_values()
            
        try:
            with open(filepath, 'w') as f:
                json.dump(self.processed, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to {filepath}: {e}")
            return False


def main():
    """Main function to demonstrate the class."""
    example = ComplexExample(
        name="Test Example",
        values=[5, 10, 15, 20, 25, 30]
    )
    
    result = example.process_values()
    print(f"Processed results: {result}")
    
    output_path = Path("output.json")
    if example.save_to_json(output_path):
        print(f"Results saved to {output_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
