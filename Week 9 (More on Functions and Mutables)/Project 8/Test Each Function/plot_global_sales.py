#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:18:37 2020

@author: devinpowers
"""


import pylab


'''
indicator = platform
L1, L2 = ([0, 1980, 1981, 1982], [2530000.0, 7070000.0, 4760000.0, 7810000.0])



indicator = year

year = 1981

(['GB', 'GEN'], [20150000.0, 8690000.0])

'''

def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()
    
    
def main():
    
    indicator = 'year'
    
    x, y = (['GB', 'GEN'], [20150000.0, 8690000.0])
    
    
    value = c_value   #publusher name or year
    
    plot_global_sales(x,y,indicator, value)
    
    
if __name__ == "__main__":
    

    main()   
    