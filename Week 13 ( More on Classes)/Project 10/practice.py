#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:13:27 2020

@author: devinpowers
"""




tab = [['', 'a', 'b', 's', 'e', 't', 'w', 'x', 'w', 'a', '', '5', '5'],
 ['3', 'a', 'b', 's', 'e', 't', 'w', 'x', 'w', 'a', '9', '5', '5'],
 ['9', 'a', 'b', 's', '', 't', 'w', 'x', 'w', 'a', 'a', '5', '2'],
 ['10', '6', 'b', 's', '', '2', 'w', '9', 'w', '10', 'a', '5', '9']]


tab[0][3]
for row_list in tab:
    
    print(row_list)

Dr = 0
Dc = 0
Sr = 1
Sc = 2

'''

if tab[Dr][Dc] == "":
    print('Empty')
    tab[Dr][Dc]= tab.append(tab[Sr][Sc].pop())
    
print(tab)
'''
    
    
a, b = tab[Dr][Dc], tab[Sr][Sc]
    


    

tab[Dr][Dc]= tab.append(tab[Sr][Sc])



    
''' 
#if value in tab[Dr][Dc] == "": #empty space
 #   print('Cell is empty')

i = ['title', 'email', 'password2', 'password1', 'first_name', 'last_name', 'next', 'newsletter']

a, b = i.index('password2'), i.index('password1')

i[b], i[a] = i[a], i[b]
     
'''

   
    
    
