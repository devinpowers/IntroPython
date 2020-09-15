#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 8
@author: devinpowers
"""


''' Your header goes here '''

import csv
import pylab
from operator import itemgetter

def open_file():
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

def read_file(fp):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

   

def get_data_by_column(D1, indicator, c_value):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

def get_publisher_data(D3, publisher):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

def display_global_sales_data(L, indicator):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    
    pass
    

def get_genre_data(D2, year):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass
    
def display_genre_data(genre_list):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    header = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    
    pass

def display_publisher_data(pub_list):
    '''
        WRITE DOCSTRING HERE!
    '''
    pub = pub_list[0][0]
    header = ['Title', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    
    pass

def get_totals(L, indicator):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

def prepare_pie(genres_list):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

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

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
def main():
    
    # Menu options for the program
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
                   
    while choice != '5':
        
        #Option 1: Display all platforms for a single year
            
            try:
                
                #if the list of platforms for a single year is empty, show an error message    
                pass
            
            except ValueError:
                print("Invalid year.")
                
                
                
                
                
                
        
                
        #Option 4: Display publisher data
            
                # Enter keyword for the publisher name
                
                # search all publisher with the keyword
                match = []
                
                # print the number of matches found with the keywords
                if len(match) > 1:    
                    print("There are {} publisher(s) with the requested keyword!".format(len(match)))
                    for i,t in enumerate(match):
                        print("{:<4d}{}".format(i,t[0]))
                    
                    # PROMPT USER FOR INDEX
                    
                else:
                    index = 0
                
        choice = input(MENU)
    
    print("\nThanks for using the program!")
    print("I'll leave you with this: \"All your base are belong to us!\"")

if __name__ == "__main__":
    main()
