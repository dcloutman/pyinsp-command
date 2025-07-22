#!/usr/bin/env python3
"""Example of an invalid Python script with syntax errors."""

import sys

def main():
    """Main function with syntax errors."""
    print("This line is fine")
    
    # Missing closing quote - syntax error
    print("This string is not closed properly
    
    # Missing colon - syntax error  
    if True
        print("Missing colon above")
    
    # Indentation error
  print("Wrong indentation")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
