#!/usr/bin/env python3

import os
import sys
import getpass



dpath           = os.path.dirname(os.path.realpath(__file__))
passwords_fpath = os.path.join(dpath, 'most-common.csv')




try:
	conn     = open(passwords_fpath, 'r')
except IOError:
	print(passwords_fpath + ' - the list of bad passwords - not found. Did you delete it?')
	sys.exit(1)
else:
	contents = conn.read()
	conn.close()





bad_passwords = set(contents.split(','))






def main (args):

	if args['secure']:

		password = getpass.getpass("[password123] enter your password:")
		print(password in bad_passwords)

	else:
		for password in args['passwords']:
			print(password in bad_passwords)
