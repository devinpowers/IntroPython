#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Formatting Output for Strings
@author: devinpowers
"""

#import math
'''Formatting'''

#print('{} is {} years old'.format("Bill",25))


#print("{} is nice but {} is divine!".format(1,math.pi))


''' Width and Alignment Descriptors'''

#print(("{:>10s} is {:<10d}years old.".format('Devin',25)))



''' Floating-Point Precision Descriptor '''

#notice the spaces
#floating point allows you to control the number of decimals
#print(math.pi)
#print("Pi is {:.4f}".format(math.pi))
#print("Pi is {:8.4f}".format(math.pi))
#print("Pi is {:8.2f}".format(math.pi))

#there is % floating-point descriptor that converts from a decimal to a percent includes the insertion of the % character

#print("{:8.2%}".format(2/3))

''' Control and Strings '''

"""
''' Finding a Letter and it's Index in a word example: '''
river = "Mississippi"

target = input("Input a character to find: ")

for index, letter in enumerate(river):
    if letter == target:
        print("Letter found at index: ", index)
    
else:
    print('Letter', target, 'not found in', river)

"""


''' Enumerate Iterator'''

"""
river = "Mississippi"

for index,letter in enumerate(river):
    print(index,letter)
"""  
  
''' 4.6 Working with Strings '''

# Left offf at Page 250 with 10 more pages to GO!
