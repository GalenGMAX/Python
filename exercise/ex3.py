#!/usr/bin/env python

my_name = 'Galen G.'
my_age =  27 # or 28
my_height = 74 # inches
my_weight = 80 # KG
my_eyes = 'Black'
my_teeth = 'Yellow'
my_hair = 'Black'

print "let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the smoke." % (my_teeth)

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age,my_height,my_weight,my_age+my_height+my_weight)

