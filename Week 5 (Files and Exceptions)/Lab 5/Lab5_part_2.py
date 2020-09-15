#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:52:13 2020

@author: devinpowers
"""



fp = open('data.txt')  # open the file; set breakpoint

for line in fp.readlines():
    name = line[0:12]
    height = line[12:16]
    weight = line[24:29]
    
print(name)