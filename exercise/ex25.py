#!/usr/bin/env python
# -*- coding:utf-8 -*-

str_space="""This function will break up words for us."""
str_comma="apple,pear,orange,strawberry,peach,banana,pineapple,watermellon"

print str_space.split(" ")

print str_comma.split(",")

print str_space.split(" ").pop(0)

print str_comma.split(",").pop(1)

print str_comma.split(",").pop(-1)

print sorted(str_comma.split(","))


