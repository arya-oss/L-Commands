#!/usr/bin/env python

#@author Rajmani Arya

import sys
import os
import argparse
import tempfile

from subprocess import call

def main():
	description="Open file in any text editor"
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("-e", "--editor", type=str, help="Provide existing editor e.g, -e nano or -e vi")
	parser.add_argument("filename", type=str, help="Provide filename to edit")
	args = parser.parse_args()
	# print args.editor, args.filename
	prev_data = ''
	if os.path.isfile(args.filename):
		f = open (args.filename, 'r')
		prev_data = f.read()
		f.close()

	editor = args.editor if args.editor else 'vi'

	with tempfile.NamedTemporaryFile(suffix=args.filename) as tf:
		tf.write(prev_data)
		tf.flush()
		call([editor, tf.name])
		tf.seek(0)
		final_data = tf.read()
		with open(args.filename, 'w') as f:
			f.write(final_data)

	sys.exit(0)

if __name__=='__main__':
	main()	