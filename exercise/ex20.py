#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import argv

def print_all(file):
	print file.read()

def rewind(file):
	file.seek(0)

def tell(file):
	print "tell",file.tell()

def print_a_line(line_count,file):
	print line_count, file.readline()

current_file=open("./ex16_write.txt","r+")
tell(current_file)

print_all(current_file)

tell(current_file)

rewind(current_file)

tell(current_file)

print_a_line(1,current_file)

tell(current_file)

print_a_line(3,current_file)

tell(current_file)
