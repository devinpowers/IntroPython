#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:36:42 2020

@author: devinpowers
"""



import csv
import pylab
from operator import itemgetter

def open_file():
    
    ''' Open File here, try and Except suite '''
    
    while True:  
        file_name = input("Input a file name: ")
        try:
            fp = open(file_name,'r', encoding = 'utf-8')
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            continue
    return fp




def read_file(fp):
    '''
       Read file, and create Dictionaries, Create new Dictionaries and sort, return 3 new dictionaries
    '''
    # skip header
    fp.readline()
    data_reader = csv.reader(fp)

    D1 = {}
    D2 = {}
    D3 = {}

    for line in data_reader:
    
        name = line[0].lower()
        platform = line[1]
        
        if line[2] == 'N/A':
            year = 0
        else:
            year = int(line[2])
       
        genre = line[3].lower()
        publisher = line[4].lower()
        na_sales = float(line[5]) *1000000
        europe_sales = float(line[6])*1000000
        japan_sales = float(line[7])*1000000
        other_sales = float(line[8])*1000000
    
        global_sales = (na_sales + europe_sales + japan_sales + other_sales)
    
        #Start Making New Dictionaries 
        D1[name] = [name,platform, year, genre, publisher, global_sales]
    
    #You need to make the values of your dictionary an array of tuples. Then you can append new tuples instead of overwriting them. 

        if genre in D2:
            D2[genre].append((genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales))
        else: 
            D2[genre] = [(genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)]
        
        
        if publisher in D3:
            D3[publisher].append((publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales )) 
        else:
            D3[publisher] = [(publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales)]
            
        
        # Sort Dictionary 1
        D1_new = {}
        
        for key, value in sorted(D1.items()):
            D1_new[key] = value
    
    
        # Sort DIctionary 2
        D2_new = {}
        
        for key, val in sorted(D2.items()):
            D2_new[key] = sorted(val, key=itemgetter(-1), reverse = True)

        # Sort Dictionary 3
        D3_new = {}
    
        for key,val in sorted(D3.items()):
            D3_new[key] = sorted(val, key=itemgetter(-1), reverse=True)
    
    
    
    return D1_new, D2_new, D3_new
  
  
    
def main():
    
    #open the file
    fp = open_file()
    
    #Read the file
    
    D1_new, D2_new, D3_new = read_file(fp)
    
    print('Dict 1:', D1_new)
    print('\n')
    print('Dict 2:', D2_new)
    print('\n')
    print('Dict 3:', D3_new)
    
if __name__ == "__main__":
    main()   
    