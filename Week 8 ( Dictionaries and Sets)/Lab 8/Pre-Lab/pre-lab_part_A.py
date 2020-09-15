#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:42:57 2020

@author: devinpowers
"""
M = { 200: "EE", 100: "ME", 500: "CPS" }

A = 100 in M
print( "A:", A )              # A:

B = "ME" in M
print( "B:", B )              # B:


print( "M[100]:", M[100] )    # M[100]:

# change value in M
M[500] = "CS"
print( "M[500]:", M[500] )    # M[500]:
    
    

print( "M.keys():" )          # M.keys():
for key in M.keys():
    print( key )

print( "M.values():" )        # M.values():   
for value in M.values():
    print( value )

print( "M.items():" )         # M.items():
for key, value in M.items():
    print( key, value )


# keys
print( "M:" )                 # M:
for X in M:
    print( X )
