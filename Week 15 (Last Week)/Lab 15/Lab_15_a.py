#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:03:21 2020

@author: devinpowers
"""


import pandas #import pandas module
import time  #used to calculate execution time
import csv  #import csv module


def read_csv_1(filename):
    ''' This function read a csv file into a list of lists (each line is an element)
    Returns: list of lists'''
    pass


def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''
    pass
    
def find_median_1(data, index):
    '''This function receives a list of lists (data) and an integer index as input 
    and calculates and prints the median of the column index'''
            
    pass          



def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input 
    and calculates and prints the median of the column name'''
    pass
    
    
def main():
    filename = "college_scorecard.csv"
    
    start_time = time.time()
    #REPLACE: read csv file using csv module
    time1 = time.time()
    print("read_csv_1: {:.4f}".format((time1 - start_time)*1000))
    
    start_time = time.time()
    #REPLACE: read csv file using pandas module
    time2 = time.time()
    print("read_csv_2: {:.4f}".format((time2 - start_time)*1000))
    
    index = 1
    column = '' #replace with the method to retrieve 
                #the column name 
    
    
    start_time = time.time()
    median_1 = 0 #REPLACE: find the median using lists
    time3 = time.time()
    print("find_median_1 time: {:.4f}".format((time3 - start_time)*1000))
    print("Median: ", median_1)
    
    start_time = time.time()
    median_2 = 0 #REPLACE: find the median using pandas
    time4 = time.time()
    print("find_median_2: {:.4f}".format((time4 - start_time)*1000))
    print("Median: ", median_2)
    
    
if __name__ == '__main__':
    main()