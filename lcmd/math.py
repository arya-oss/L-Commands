#!/usr/bin/env python

#@author Rajmani Arya

import sys
import os
import argparse

def main():
	description="""Perform Mathematical Operations
		allowed operations add|sub|mul|div|pow|bin|hex
	"""
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("ops", type=str, help="Provide mathematical operation name")
	parser.add_argument("nums", nargs="+", type=float, help="Provide integer args")
	args = parser.parse_args()

	if args.ops == "add":
		s = 0
		for i in args.nums:
			s += i
		print s

	elif args.ops == "sub":
		s = args.nums[0]
		for i in args.nums[1:]:
			s -= i
		print s

	elif args.ops == "mul":
		s = args.nums[0]
		for i in args.nums[1:]:
			s *= i
		print s

	elif args.ops == "div":
		if len(args.nums) != 2:
			print 'Two args as number required !'
			sys.exit(1)
		if args.nums[1] == 0:
			print 'Err: 2nd number is 0'
			sys.exit(1)
		print float(args.nums[0])/float(args.nums[1])

	elif args.ops == "bin":
		if len(args.nums) != 1:
			print 'Only one argument required !'
			sys.exit(1)
		if str(int(args.nums[0])).isdigit() == False:
			print 'Only integer argument accepted !'
			sys.exit(1)
		print format(int(args.nums[0]), 'b')

	elif args.ops == "hex":
		if len(args.nums) != 1:
			print 'Only one argument required !'
			sys.exit(1)
		if str(int(args.nums[0])).isdigit() == False:
			print 'Only integer argument accepted !'
			sys.exit(1)
		print format(int(args.nums[0]), 'x')

	else:
		print 'Invalid ops, see math --help for more details'

	sys.exit(0)

if __name__=='__main__':
	main()	