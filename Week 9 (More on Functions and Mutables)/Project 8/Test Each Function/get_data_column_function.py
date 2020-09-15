#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check Get Data Column

indicator = year

c_value = 1981

"""

from operator import itemgetter

def get_data_by_column(D1, indicator, c_value):
    '''
        Have to fix if the c_value isnt given!!
    '''
    new_list_of_tuple = []
    # sort List by Global Sales Largest to smallest
    
    if indicator == 'year':
        
        for value in D1.values():
            if value[2] == c_value:
                
                new_tuple = (value[0],value[1], value[2],value[3],value[4],value[5])
            
                new_list_of_tuple.append(new_tuple)
    
        new_list_of_tuple.sort(key= itemgetter(-1,1), reverse = True )
    
    elif indicator == 'platform':
        
        for value in D1.values():
                if value[1] == c_value:
                    
                    new_tuple = (value[0],value[1], value[2],value[3],value[4],value[5])
            
                    new_list_of_tuple.append(new_tuple)
                   
        new_list_of_tuple.sort(key= itemgetter(-1,2), reverse = True )
                    
    #sort new_list_tuple              
  
    return new_list_of_tuple





''' Inputs '''

'''
D1 ={'asteroids': ['asteroids', '2600', 1980, 'shooter', 'atari', 4310000.0],
 'burgertime': ['burgertime','2600',1981,'puzzle','mattel interactive',590000.0],
 'e.t.: the extra terrestrial': ['e.t.: the extra terrestrial','2600',1981,'action','atari',1970000.0],
 frogger': ['frogger', '2600', 1981, 'action', 'parker bros.', 2200000.0],
 'missile command': ['missile command', '2600', 1980, 'shooter', 'atari', 2760000.0],
 'pac-man': ['pac-man', '2600', 1982, 'puzzle', 'atari', 7810000.0],
 'pokemon x/pokemon y': ['pokemon x/pokemon y','3DS',  2013,  'role-playing','nintendo',14600000.0],
 space invaders': ['space invaders','2600',0,'shooter','atari',2530000.0]}

indicator = year

c_value = 1981

'''
'''Output'''
'''

[('frogger', '2600', 1981, 'action', 'parker bros.', 2200000.0),
 ('e.t.: the extra terrestrial', '2600', 1981, 'action', 'atari', 1970000.0),
 ('burgertime', '2600', 1981, 'puzzle', 'mattel interactive', 590000.0)]

'''








