#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:44:15 2020

@author: devinpowers
"""


# making a dictonary
M = {}
M[ "Joyce" ] = 7
M[ "Mike" ] = 12
M[ "Bea" ] = 9 

print( "M:", M )   

if "Bea" in M:
    A = M[ "Bea" ]
    print( "A:", A )

# deleting a key-value in the dictonary
if "Joyce" in M:
    del M[ "Joyce" ]

print( "M:", M )  