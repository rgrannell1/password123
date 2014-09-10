#!/usr/bin/env python3

"""
password123

Usage:
	password123 <password> ...
	password123 (-h | --help | --version)

"""

from docopt      import docopt
from password123 import main

if __name__ == '__main__':

	arguments = docopt(__doc__, version = "0.1.0")

	main(arguments['<password>'])
