#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get_totals Function
@author: devinpowers
"""
'''
L = [('pac-man', '2600', 1982, 'puzzle', 'atari', 7810000.0),
 ('asteroids', '2600', 1980, 'shooter', 'atari', 4310000.0),
 ('missile command', '2600', 1980, 'shooter', 'atari', 2760000.0),
 ('space invaders', '2600', 0, 'shooter', 'atari', 2530000.0),
 ('frogger', '2600', 1981, 'action', 'parker bros.', 2200000.0),
 ('e.t.: the extra terrestrial', '2600', 1981, 'action', 'atari', 1970000.0),
 ('burgertime', '2600', 1981, 'puzzle', 'mattel interactive', 590000.0)]

indicator = 'platform'
c_value = '2600'
'''


'''
 
indicator = 'year'


L = [('super mario land 2: 6 golden coins','GB',1992,'adventure','nintendo',11180000.0),
 ('sonic the hedgehog 2', 'GEN', 1992, 'platform', 'sega', 6020000.0),
 ("kirby's dream land", 'GB', 1992, 'platform', 'nintendo', 5130000.0),
 ("the legend of zelda: link's awakening",'GB',1992,'action','nintendo',3840000.0),
 ('mortal kombat', 'GEN', 1992, 'fighting', 'arena entertainment', 2670000.0)]


'''

'''
L = [('baseball', 'NES', 1983, 'sports', 'nintendo', 3200000.0),
 ('jr. pac-man', '2600', 1983, 'puzzle', 'atari', 780000.0),
 ('crystal castles', '2600', 1983, 'action', 'atari', 770000.0),
 ("mr. do!'s castle", '2600', 1983, 'action', 'parker bros.', 160000.0)]


'''



def get_totals(L, indicator):
    
    '''
        Build Two list (L1, L2) of Corresponding Values with L1 being  each year or each platform, and  
        L2 being the corresponding gloabl sales for that year or platform.
        Built a Dictionary with Key being either year or platform, then the Value equal to the
        global sales.
           
    '''
    
    if indicator == 'year':
        
        D = {}

        for platform in L:
            if platform[1] in D:
                D[platform[1]] += platform[5]    #If platform already in Dictionary, add gloabl sales
            else:
                D[platform[1]] = platform[5]     #Else, platform hasnt been entered in the dictionary yet so we enter it in with global sales as its value
                
        L1 = []  # list of platforms
        L2 = []  # corresponding list of global sales for each platform
        
        for keys in D.keys():
            L1.append(keys)   #add platform to L1
        
        L1.sort()                        # Sort L1
        L2 = [D[v] for v in L1]          # Add corresponding Value (global sales) to L2 from reading L1
    
  
    
    elif indicator == 'platform':
        
        D = {}
        
        for year in L:
            if year[2] in D:           # If year already in Dictionary, we add global sales
                D[year[2]] += year[5]
            else:             
                D[year[2]] = year[5]    # Else, year hasnt been added yet, so we enter it in as a key and set gloabl sales as its value
        
        L1 = []   # list of years
        L2 = []   # corresponding list of global sales for each year

        for keys in D.keys():
            L1.append(keys)          # adds year to L1
        
        L1.sort()
        L2 = [D[v] for v in L1]     # adds corresponding Value (global sales) to L2 from reading L1
        
    return L1, L2


