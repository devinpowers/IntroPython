#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab Exercise #2

Part 2: Programming with Control Structures

@author: devinpowers
"""


n_str = input("Input an integer (0 terminates): ")

# convert to int

n_int = int(n_str)

# Good stuff goes here

odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0

positive_int_count = 0

while n_int != 0:
    
    if n_int < 0:
        continue
    elif n_int % 2 == 0:
        
        even_sum += n_int
        even_count += 1
    else:
        #must be odd
        odd_sum += n_int
        odd_count += 1
    
    positive_int_count += 1
    
    n_int = int(input("Input an integer (0 terminates): "))
    
    
        
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)

