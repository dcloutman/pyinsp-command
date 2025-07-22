#!/usr/bin/env python3
"""
Valid Python file for testing.
"""

import sys
import os


def main():
    """Main function."""
    print("Hello, World!")
    print(f"Python version: {sys.version}")
    
    # Calculate something
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}, Average: {average}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
