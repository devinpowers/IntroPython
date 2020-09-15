#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:30:58 2020

@author: devinpowers
"""

data_map = {'Asia':{'China': ['Hong Kong',' Beijing', 'Shanghai'], 'Japan': ['Tokyo']}, 'Europe':{'Germany': ['Berlin'], 'France': ['Paris', 'Nice']}}


            
           
def display_map( data_map ):

    # Modify this code to display a sorted nested dictionary
    continents_list = [] #sorted list of the continent keys
    
    for continent, countries in data_map.items():
        
        
        continents_list.append(continent)
        continents_list.sort()
         
        for continents in continents_list:
            print("{}:".format(continents)) #continents in continents_list
            
    
        countries_list = [] #sorted list of the countries keys in the continents

            for country, cities in countries.items():
                countries_list.append(country)
                
                countries_list.sort()
                
                for countries in countries_list:
                    
                    print("{:>10s} --> ".format(countries),end = '') #countries in countries_list
                
                

display_map(data_map)