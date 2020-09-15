#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:00:18 2020

https://www.youtube.com/watch?v=C26lA9dGubo
@author: devinpowers

Building a Card Deck
"""

# match the code you're in

import random

class Card(object):
    
    def __init__(self,name,value, suit):
        
        self.value = value
        self.suit = suit
        self.name = name
        
    def __repr__(self):
        return str(self.name) + " of " + self.suit
    
    
class StandardDeck(list):
    
    def __init__(self):
        suits = ["Hearts", "Spades","Diamonds", "Clubs"]
        
        values = {"two":2,
                  "Three":3,
                  "Four":4,
                  "Five":5,
                  "Six":6,
                  "Seven":7,
                  "Eight":8,
                  "Nine":9,
                  "Ten":10,
                  "Jack":11,
                  "Queen":12,
                  "King":13,
                  "Ace":14}
        

        for name in values:
            for suit in suits:
                self.append(Card(name, values[name], suit))
    
    def __repr__(self):
        
        return "Standard deck of cards:{0} remaining".format(len(self.cards))

    def shuffle(self, times=1 ):
    
        random.shuffle(self.cards)
        print("Deck Shuffled")

    def deal(self):
        
        return self.cards.pop(0)
        
        
    

            
        
        
    
