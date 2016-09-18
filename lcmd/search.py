#!/usr/bin/env python

#@author Rajmani Arya

import sys
import os
import argparse
from subprocess import call

def main():
	description="Search text in File or file in Folder"
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('arg1', type=str, help='pattern to search')
	parser.add_argument('arg2', type=str, help='filename or directory')
	args = parser.parse_args()

	if os.path.isdir(args.arg2):
		call(['ls -a '+ args.arg2 +' | grep '+args.arg1 ], shell=True)
	else:
		call(['grep '+args.arg1+' '+args.arg2 ], shell=True)

	sys.exit(0)

if __name__=='__main__':
	main()	