#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:34:46 2020

@author: devinpowers
"""

import collections
from operator import itemgetter
import csv
from collections import OrderedDict

fp = open('tiny_games.csv','r')

fp.readline()
data_reader = csv.reader(fp)


D1 = {}
D2 = {}
D3 = {}


for line in data_reader:
    
    name = line[0].lower()
    platform = line[1]
    if line[2] == 'N/A':
        year = 2020   # suppose to ignore it
    else:
        year = int(line[2])
            
    genre = line[3].lower()
    publisher = line[4].lower()
    na_sales = float(line[5]) *1000000        #na_sales = North America Sales
    europe_sales = float(line[6])*1000000
    japan_sales = float(line[7])*1000000
    other_sales = float(line[8])*1000000
    
    # Global Sales
    
    global_sales = (na_sales + europe_sales + japan_sales + other_sales)
    
    
    D1[name] = [name,platform, year, genre, publisher, global_sales]
    

    if genre in D2:
        D2[genre].append((genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales))

    else:
        D2[genre] = [(genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)]
        
    
    if publisher in D3:
       D3[publisher].append((publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales ))
        
    else:
        D3[publisher] = [(publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales)]
        
    
    ''' Sort Dictionaries '''
    # Sort Dictionary 1
    
    D1_new = {}
        
    for key, value in sorted(D1.items()):
        D1_new[key] = value
    
    # Sort DIctionary 2
   
    D2_new = {}

    for key, val in sorted(D2.items()):
        D2_new[key] = sorted(val, key=itemgetter(-1), reverse = True)
                             
                    
    # sort Dictionary 3

    D3_new = {}
    
    for key,val in sorted(D3.items()):
        D3_new[key] = sorted(val, key=itemgetter(-1), reverse=True)
        
        
        
        
        
        
        
    
    

             
    

  
    
    

            
            
            
        
      
        
      
    
            
            
            
            
            
    








