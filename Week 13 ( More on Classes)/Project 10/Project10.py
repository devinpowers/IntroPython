#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:55:21 2020

@author: devinpowers
"""


''' Your header goes here '''

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)


def initialize():
    '''
        Shuffling a deck of Cards and Initializing it into a tableau of 4 rows and 13 coloumns
        
    '''
    stock = cards.Deck()
    stock.shuffle()
    
    tableau = [ [],[],[],[] ] # list of 13 lists, which will have 4 cards
    
    x = 0
    while not stock.is_empty():
        tableau[x].append(stock.deal())
        x += 1
        if x == 4:
            x=0
    
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()



def validate_move(tableau,source_row,source_col,dest_row,dest_col):
    '''
        If the Move is valid!
    '''


    pass

def move(tableau,source_row,source_col,dest_row,dest_col):
    '''
        Move within the Tableau!
    '''

    sr = source_row
    sc = source_col
    dr = dest_row
    dc = dest_col
    
    
    
    pass
    


def check_win(tableau):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass

def shuffle_tableau(tableau):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    pass
             
def main():
    '''
        WRITE DOCSTRING HERE!
    '''
    command = input("Your move: ").lower() # incase you get Q instead of q
    
    while command != 'q':
        try:
            
    pass

if __name__ == "__main__":
    main()  