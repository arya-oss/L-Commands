#!/usr/bin/env python

#@author Rajmani Arya

import sys
import os
import argparse

from subprocess import call

lang_cmds = {
	'c': 'gcc',
	'cpp': 'g++',
	'py': 'python',
	'rb': 'ruby',
	'sh': 'sh',
	'js': 'node',
	'jv': ['javac', 'java']
}

def main():
	description='''
		compile and run filename in any lang.
		PARAMS = {c,cpp,py,rb,sh,js,java}
	'''
	parser = argparse.ArgumentParser(description=description)

	parser.add_argument('lang', type=str, help='Provide programming languages')
	# parser.add_argument('-p', '--params', type=str, help='Provide optional parameters')
	parser.add_argument('filename', type=str, help='Provide source code filename')
	args = parser.parse_args()
	
	if lang_cmds[args.lang] is None:
		print 'Language not supported'
		sys.exit(1)
		
	# params = None
	# if args.params is not None:
	# 	params = args.params

	# Compile code
	if args.lang != 'jv':	
		ret = call([lang_cmds[args.lang], args.filename])
	else:
		ret = call(['javac', args.filename])

	# Run file if it is not scripting language
	if ret == 0 and args.lang in ['c', 'cpp']:
		call(['./a.out'])
	elif ret==0 and args.lang == 'jv':
		call(['java', args.filename.split('.')[0]]) 

	sys.exit(0)

if __name__=='__main__':
	main()	