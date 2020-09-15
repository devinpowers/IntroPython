#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 4 Part B, C, and D

@author: devinpowers
"""

""" Leap Year """

def leap_year(year):
    ''' Georgian Leap year '''
    year = int(year)
    return True if year %400 == 0 or (year % 4 == 0 and year % 100 !=0) else False

""" Rotate """
 # assume str for s and int for n
def rotate(s,n):
    ''' Rotates word by n size '''
    return s[-n:]+s[:-n]

""" Digit Count """

def digit_count(numbers):
   '''returns a count of even, odd, and zeros that are too the left of the decimal '''
   even = '2468'
   odd = '13579'
   even_count = 0
   odd_count = 0
   zero_count = 0
   for n in numbers: 
       if n == '.': 
           break
       if n in even:  
           even_count += 1
       if n in odd:
           odd_count +=1
       if n == '0': 
           zero_count += 1
   return even_count,odd_count,zero_count
  
           
""" Float Check """

def float_check(string):
    '''float check '''
    new_str = ''
    decimal = '.'
    if decimal in string:
        new_str = string.replace('.','0')
    else:
        new_str = string
    #now check if digit
    return True if new_str.isdigit() else False

    
    

        
        
        
        