#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:08:12 2020

https://www.youtube.com/watch?v=tmY6FEF8f1o

@author: devinpowers
"""

import turtle

class Polygon:
    
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        self.interior_angles = (self.sides - 2)*180
        self.angle = self.interior_angles/self.sides
        
    
    def draw(self):
        
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180-self.angle)
        turtle.done()
        
        
        

        
        
        


square = Polygon(4,"Square")

pentagon = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)


print(pentagon.sides)
print(pentagon.name)


hexagon = Polygon(6, "Hexagon")

hexagon.draw()