#!/usr/bin/env python

from sys import argv

print argv
print len(argv)

print "unpacking argv(s)..."
script, first, second, third = argv
print script
print first
print second
print third


