#!/usr/bin/env python

"""
password123

Usage:
	password123 <password> ...
	password123 (-s | --secure)
	password123 (-h | --help | --version)

Version:
	0.1.0

Description:
	password123 checks if an input password is ranked among the 10,000 most
	commonly used, as measured by xato.net. Such passwords are unfit for use,
	as they will be the first guesses during a brute-force attack.

Arguments:
	<password>      The passwords to check for membership in the 10,000 most
	                commonly used passwords.

Options:
	-s, --secure    Should password123 securely prompt for your password?
	                This is a good idea if you indent to use the password
	                you are checking is actually your password.
    --version       Show the version number.
"""

from docopt      import docopt
from password123 import main





if __name__ == '__main__':

	arguments = docopt(__doc__, version = "0.1.0")

	main({
		"passwords": arguments['<password>'],
		"secure":    arguments['--secure'] or arguments['-s']
	})
