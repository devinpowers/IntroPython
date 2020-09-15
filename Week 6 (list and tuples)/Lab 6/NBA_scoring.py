#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:11:22 2020

@author: devinpowers
"""


fp = open("NBA.txt")
counter = 0

player_list = []
total_list = [0,0,0,0]

print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Game One", "Game Two", "Game Three", "Game Four", "Mean"))

for line in fp:
    counter += 1

    line = line.strip("\n").strip()
    line = line.split()
    
    
    
    name = line[1] + " " + line[0]
    game_one = int(line[2])
    game_two = int(line[3])
    game_three = int(line[4])
    game_four = int(line[5])
    average = (game_one+game_two+game_three+game_four)/4
    average = round(average,2)
  
    total_list[0] += game_one
    total_list[1] += game_two
    total_list[2] += game_three
    total_list[3] += game_four
    
    
    
    tuple = (name, game_one, game_two, game_three, game_four, average)
    player_list.append(tuple)
    
player_list_sorted = sorted(player_list)


for item in player_list_sorted:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(item[0], item[1], item[2], item[3], item[4], item[5]))
    
   
mean_list = [total_list[0]/counter,total_list[1]/counter,total_list[2]/counter,total_list[3]/counter]




fp.close()