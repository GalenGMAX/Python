#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ex15_import import hello_world

hello_world()

f=file("./ex15_import.py")

content=f.read()

print content

