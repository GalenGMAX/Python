#!/usr/bin/env python
# -*- coding:utf-8 -*-

#f=open("./ex16_write.txt","r+")

f=open("./ex16_write.txt","a+")

#f.truncate()
#print "file truncated."

print "input what you want to append to the file"
f.write(raw_input("-->"))

print "content written, reading edited file"

f_r=open("./ex16_write.txt","r")
print f_r.read()

f_r.close()

f.close()


