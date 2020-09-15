#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:21:29 2020

@author: devinpowers
"""


#################################
## CSE 231
## Debug exercise for Lab 5
## print() not allowed
## @amirootyet
#################################

fp = open('data.txt')  # open the file; set breakpoint
total_height = 0       # keep track of total height

for line in fp.readlines()[1:]:
    name = line[:20]
    height = line[12:20]
    
    total_height += float(height.strip())
    
fp.close()

fp = open('data2.txt', 'w')  # open another file in write mode
fp.write(str(total_height))



#part 2


fp = open('data.txt')  # open the file; set breakpoint

for line in fp.readlines():
    name = line[0:12]
    height = line[12:16]
    weight = line[24:29]



