#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:29:43 2020

Prepare Pie Function

@author: devinpowers
"""

from operator import itemgetter

'''

genres_list = [ ('Aenre1', 23, 232, 232, 2, 2, 232, 223),
               ('Cenre3', 23, 232, 232, 2, 2, 232, 235),
               ('Fenre2', 23, 232, 232, 2, 2, 232, 23235),
               ('Jenre31', 23, 232, 232, 2, 2, 232, 233),
               ('KGenre23', 23, 232, 232, 2, 2, 232, 2673),
               ('Genre232', 23, 232, 232, 2, 2, 232, 2873),
               ('Genre6', 23, 232, 232, 2, 2, 232, 2343),
               ('Benre22', 23, 232, 232, 2, 2, 232, 567),
               ('Genre45', 23, 232, 232, 2, 2, 232, 783),
               ('Genre67', 23, 232, 232, 2, 2, 232, 24673),
               ('Genre87', 23, 232, 232, 2, 2, 232, 90)
               
               
               ]


'''


def prepare_pie(genres_list):
    '''
        Prepare pie for genre list stuff, return 2 lists:
    '''
     
    list_of_tuples = []

    for element in genres_list:
    
        genre_sales = (element[0], element[7])  # Genre name and Global Sales
    
        list_of_tuples.append(genre_sales)  
    
    
    list_of_tuples.sort(key = itemgetter(1), reverse = True) #sort by Genre Name first, then by Global Sales

    L1 = []  #Genre Name

    L2 = []  #Corresponding Global Sales

    for pair in list_of_tuples:
    
        L1.append(pair[0])
    
        L2.append(pair[1])
    
    return L1, L2

