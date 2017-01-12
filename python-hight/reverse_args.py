#!/usr/bin/python

import sys

args=sys.argv[1:]
for arg in args:
    print arg
args.reverse()
for arg in args:
    print arg


