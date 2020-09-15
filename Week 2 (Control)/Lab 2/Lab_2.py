#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 2: Control

@author: devinpowers
"""


n_str = input("Input an integer (0 terminates): ")

n_int = int(n_str)

# Good stuff goes here


odd_sum = 0
odd_count = 0
even_sum = 0
even_count = 0
positive_int_count = 0

while n_int != 0:
    
    #if given odd number
    if n_int < 1:
        continue
    #if given number is even
    elif n_int %2 ==0 :
        even_sum += n_int
        even_count += 1
        positive_int_count += 1
    # if number is odd
    else:
        odd_sum += n_int
        odd_count += 1
        positive_int_count += 1
    
    n_int = int(input("Input an integar (0 terminates):"))
        
    
    
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)


