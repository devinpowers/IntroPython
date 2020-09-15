#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:45:11 2020

@author: devinpowers
"""


import clock

A = clock.Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = clock.Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = clock.Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = clock.Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )