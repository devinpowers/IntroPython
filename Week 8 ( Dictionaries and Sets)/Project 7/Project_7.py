#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



Project 7
CSE 231

@author: devinpowers
"""

import math
import csv


def open_file():
    """
    prompt for file name
    try to open the file
    except FileNotFoundError
        print error message
    :return: fp
    """ 
    while True:
        file_name = input("Input a file name: ")
        
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")          
    return fp

def calc_multipliers():
    '''creating a list multipler (m) function here '''
    # empty list
    m = []
    n = 2
    while n <= 60:
        multiplier = 1/math.sqrt(n*(n-1))
        m.append(float(multiplier))
        n += 1
    return m


def calc_priorities(state,population,m):
    ''' This Function takes the 'State' and 'Population' given, and uses the 'multipliers (m)' to create a tuple of priorities for the Given State '''
    ''' This Function isn't called in the Main program, you could use this function on its own, if you would like '''
    
    list_state_priorities = []
    tuple_state_priorities = ()
    
    for value in m:
        priority = value * population
        
        list_state_priorities.append((int(priority),state))
    
    list_state_priorities_sorted = sorted(list_state_priorities,reverse = True)
    
    #list into tuple
    
    tuple_state_priorities = tuple(list_state_priorities_sorted)
        
    return tuple_state_priorities



def read_file_make_priorities(fp,multipliers):
    
    state_reps = []
    priorities_tuple = ()
    priorities = []
    count = 1
    
    #skip header
    fp.readline()
    data_reader = csv.reader(fp)
    
    for row in data_reader:   
        # Skip line/continue to next iteration if Puerto Rico or District of Columbia 
    
        if row[1] == 'Puerto Rico' or row[1] == 'District of Columbia':
            continue
        else:
            state = row[1].replace('"','')      # Removing States name strings that have double quotes in the File!!
            population = row[2]
            
            # list of states and its inital representive value of 1
            list_of_list = [state, count]
            state_reps.append(list_of_list)
            
            # call calc_multiplers to get the list of multipliers
            multipliers = calc_multipliers()

            for multipler in multipliers:
            
                priority = multipler * int(population)
                
                priorities.append(((int(priority)),state))
                            
    # sorting fixes
    priorities_sorted = sorted(priorities, reverse = True)
    
    #list into tuple 
    ''' MIGHT have to fix here, because i need the first 385 with the hhighest priority!!! '''
    priorities_tuple = tuple(priorities_sorted)
    
    #big list of priority tuples [(priority, state), ()]
    
    priorities = list(priorities_tuple)[:385]
    
    #sort state reps alphabetically state_reps = [['State, rep #],..]
    
    state_reps = sorted(state_reps)

    return  priorities, state_reps
    

def add_to_state(state,state_reps):
    
    '''Takes the State given, finds it in our state reps lists and adds one to its representive count '''
 
    for element in state_reps:
        # if first index[0] is equal to the State given, we add one to the Representive count
        if element[0] == state: 
            element[1] += 1
   
def display(state_reps):
    
    ''' Displays Everything '''
    
    print("{:<15s}{:>4s}".format("State","Representatives"))
    
    for element in state_reps:
        state = element[0]
        number_of_reps = element[1]
        
        print("{:<25s}{:>d}".format(state, number_of_reps))
        
        
def main():
    ''' Main function calls all the above Functions '''

    #calculate the multiplers
    m = calc_multipliers()
    
    #Open the file to be read here
    fp = open_file()
    
    # read the file, make priorite tuple and the list of list with the State and number of Reps
    priorities, state_reps = read_file_make_priorities(fp, m)
    
    # for each state, send to add_state function to update the Representives
    for state_priority in priorities:
        
        add_to_state(state_priority[1],state_reps)
    
    # call display funciton
    
    display(state_reps)
    
    
    

if __name__ == "__main__":
    main()