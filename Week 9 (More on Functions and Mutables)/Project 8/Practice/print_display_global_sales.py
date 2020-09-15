#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Display Global Sales Data Function

indicator = 'year'
c_value = 1981

"""
def display_global_sales_data(L, indicator):
    
    '''Display Gloabal Sales'''
    

    if indicator == 'year':
        
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        
        sum_of_global = 0
    
        for element in L:
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(element[0],str(element[2]),element[3],element[4],element[5]))
            
            sum_of_global += element[5]

        print("\n{:90s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global)) 
    
    elif indicator =='platform':
        
         print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
         
         sum_of_global = 0
         
         for element in L:
             
              print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(element[0],element[1],element[3],element[4],element[5]))
            
              sum_of_global += element[5]
    
         print("\n{:90s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global)) 



'''Input'''
'''

indicator = 'year'
c_value = 1981

'''
'''
L =[('frogger', '2600', 1981, 'action', 'parker bros.', 2200000.0),
 ('e.t.: the extra terrestrial', '2600', 1981, 'action', 'atari', 1970000.0),
 ('burgertime', '2600', 1981, 'puzzle', 'mattel interactive', 590000.0)]

'''

''' Output '''

'''
Name                          Year      Genre               Publisher                     Global Sales
frogger                       1981      action              parker bros.                  2,200,000.00
e.t.: the extra terrestrial   1981      action              atari                         1,970,000.00
burgertime                    1981      puzzle              mattel interactive            590,000.00  

Sum of Global Sales:                                                                      4,760,000.00   
'''



    
        
        
        