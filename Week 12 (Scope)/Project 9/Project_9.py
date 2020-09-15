#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:49:25 2020

@author: devinpowers
"""


''' Your header goes here '''

import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter


def open_file():
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass


def build_dictionary(fp):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass
    

def top_affected_by_spread(master_dict):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass


def top_affected_by_numbers(master_dict):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

def is_affected(master_dict, country):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass


def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()


def affected_states_in_country(master_dict, country):

    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass


def main():
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    pass
    

    
if __name__ == "__main__":    
    main()