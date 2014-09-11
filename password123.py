#!/usr/bin/env python3

import os
import sys




try:
	conn     = open('most-common.csv', 'r', encoding = 'utf-8')
except IOError:
	print('most-common.csv - the list of bad passwords - not found. Did you delete it?')
	sys.exit(1)
else:
	contents = conn.read()
	conn.close()





bad_passwords = set(contents.split(','))






def main (args):

	if args['secure']:
		1
	else:
		for password in bad_passwords:
			print(password in bad_passwords)
