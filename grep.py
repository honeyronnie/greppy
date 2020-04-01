#!/usr/bin/env python3
"""Usage: grep.py PATTERN FILE [FILE...]

Print lines from each FILE matching regular expression PATTERN.

"""

import sys
import regex as re


def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        line = line.strip()
        if re.search(pattern, line):
            print(line)

            
def parse_argv(argv):
    """Parse script arguments."""
    if len(argv) < 2:
        raise ValueError
    pattern, paths = argv[0], argv[1:]
    return pattern, paths


def main(argv):
    """Main entry point of script."""
    try: 
        pattern, paths = parse_argv(argv)
    except ValueError: 
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    for path in paths:
        try:    
            with open(path) as file:
                grep(pattern, file)
        except FileNotFoundError as err:
            print(__doc__.strip(), file=sys.stderr)
            print(err, file=sys.stderr)
            sys.exit(1)

        
if __name__ == "__main__":
    main(sys.argv[1:])