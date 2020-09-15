#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 4

@author: devinpowers
"""

evens = '2468'
odds = '13579'

def digit_count(numInput):

    evenCount = 0
    oddCount = 0
    zeroCount = 0

    for i,num in enumerate(numInput):
        
        if num == '.':
            break
        else:
            if num in evens:
                evenCount += 1
            elif num in odds:
                oddCount += 1
            else:
                zeroCount += 1
        

    return (evenCount,oddCount,zeroCount)



    
    
