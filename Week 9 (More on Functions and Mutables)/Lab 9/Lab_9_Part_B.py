#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Lab 9: Part B

Write Program using Dictionaires of Sets

"""

def build_map( in_file1, in_file2 ):
    
    ''' build dictionary '''
    
    data_map = {}
    
    # skip headers
    in_file1.readline()
    in_file2.readline()

    #READ EACH LINE FROM FILE 1
    
    for line in in_file1:
        
        # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        # Ignore empty strings
        if continent != "":
            
            # if continent not in the dictionary, add it as a key and set the value eqaul to another dictionary
            
            if continent not in data_map:
                data_map[continent] = {}
                
                # if country is not in data_map with its corresponding continent, then add it as a Key and Set the Value equal to an empty set()
            if country not in data_map[continent]:
                data_map[continent][country] = set()
                

     #READ EACH LINE FROM FILE 2    
     
    for line in in_file2:
        
       # Split the line into two words
        countries_list = line.strip().split()
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            
            for continent in data_map:
                            
                if country in data_map[continent]:
                                  
                    if city not in data_map[continent][country]:
                        
                        
                        #instead of .append() for lists, we use .add() for sets!!!
                                      
                        data_map[continent][country].add(city)
                            
    return data_map










def display_map( data_map ):
    
    print()
    ''' Display '''
    for continent, countries in data_map.items():
        
    
        print("{}:".format(continent))
    
        for country, cities in countries.items():
            print("{:>10s} --> ".format(country),end = '')
        
            for city in cities:
                print('{}'.format(city), end= ', ')
            
            print()
            

def open_file():
    
    '''open files, try and except suite '''

    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():
    '''run main function '''

    # Empty Initial Dictionary
    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()   #close file
        in_file2.close()   #close file
        
        

if __name__ == "__main__":
    main()
