#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:52:57 2020

Lab Exercise #8 Part A

Modify a program that uses Dictionaries

@author: devinpowers
"""


import string
from operator import itemgetter


def add_word( word_map, word ):
    
    ''' Function checks if the word is in the dictionary and adds its frequency '''

    # checks if word which we just cleaned is in the dictionary, if not in dictionary it adds the word as a key and sets it equal to 0 to represent frequency
    if word not in word_map:
        word_map[ word ] = 0

    # our cleaned word is in the dictionary so we plus 1 to the frequency
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    
    ''' Take line in our file and strips/cleans word '''

    # this will take line as a complete string
    for line in in_file:

        # Splits each line in file into a list: word_list = ['line', 'in', 'File,...]
        word_list = line.split()
        #iterate through each word in the word_list
        for word in word_list:
            # removes empty string from collection of words
            if word != '-':
                # removes capitalization
                word = word.lower()
                # Each word in the word_list is stripped of any whitespaces before and after the word, and stripped of any punctuations such as periods, commas, etc
                word = word.strip().strip(string.punctuation)
                # then add_word function is called and each word is checked
                add_word( word_map, word )
        

def display_map( word_map ):
    
    ''' Displays our results in a pretty format '''

    word_list = list()

    # Adds both our word and its 'count' to a list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    #Sorts list based on alphabetical order 
    word_list.sort()
    
    # Sorts list based on index[1] the frequency
    freq_list = sorted(word_list, key=itemgetter(1),reverse= True )
    

    # Prints the Word and Count
    
    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    
    ''' Prompts for user to enter a file, file enters a try-execpt suite to check if it exisits '''
    
    file = input('Please enter a file: ')

    try:
        in_file = open( file, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

# Intial Dictionary
word_map = dict()

# Start Program by calling open_file
in_file = open_file()


#if in_file is returned:
if in_file != None:

    build_map( in_file, word_map )
    #call display_map
    display_map( word_map )
    in_file.close()
    
    
