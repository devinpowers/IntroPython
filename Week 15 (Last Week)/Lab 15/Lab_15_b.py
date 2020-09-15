#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:03:45 2020

@author: devinpowers
"""


import pandas


def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''
    pass     

def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input 
    and returns the median of the column name
    Returns: float'''
    pass
    
    
def find_highest_mpg(data_frame, country):
    '''This function receives a DataFrame and country as input and returns 
    the model of the country cars (str) with the highest mpg and the highest mpg.
    Returns: str, float'''
    pass
    
    
def main():
    filename = "mpg.csv"
    data_frame =0 #replace with the appropriate function call

    print("First 5 rows of columns mpg and horsepower:")
    print(data_frame) #replace with the correct statement
    print()

    print("Last 5 rows of columns mpg, horsepower, model_year, and name:")
    print(data_frame) #replace with the correct statement
    print()
    
    acc_median = 0 #replace with the appropriate function call
    print("Mean 0-60 mph acceleration time (in sec): {:.1f}\n".format(acc_median))
    
    car_name, country_max = 0,0 #replace with the appropriate function call
    print("Highest MPG US car:")
    print(car_name, "-", country_max, "mpg")
       
    
if __name__ == '__main__':
    main()

