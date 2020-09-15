
"""
Lab 12: Vector

"""

import math

class Vector(object):
    
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        out_str = "x: {:6.2f}, y: {:6.2f}".format(self.__x, self.__y)
        return out_str
    
    def __repr__(self):
        ''' for displaying in the shell '''
        return str(self)
    
    def __add__(self, other):
        ''' add two vectors together '''
        
        x = self.__x + other.__x
        y = self.__y + other.__y
            
        return Vector(x,y)
    
    def __sub__(self, other):
        
        '''subtracts two vectors '''
    
        x = self.__x - other.__x
        y = self.__y - other.__y
        
        return Vector(x,y)
    
    def inner(self, other):
        
        return sum(a * b for a, b in zip(self,other))
    
    def __mul__(self, other):
        
        ''' Returns the dot product of self if multipled by another Vector.
        If multiplied by an int or float, it multiplies each component by
        other.
        '''
        if type(other) == type(self):

             return self.inner(other)
        
        elif type(other) == type(1) or type(other) == type(1.0):
            
            product = tuple(a * other for a in self)
            
            return Vector(*product)
        
      
    def __rmul__(self, other):
        
        return self.__mul__(other)

    def __eq__(self, other):
        
        return self.__x == other.__x and self.__y == other.__y
    
    def magnitude(self):
        
        magnitude = math.hypot(self.__x, self.__y)
        
        return magnitude
    
    def unit(self):
        
        mag = self.magnitude()
        
        if mag == 0:
            
            raise ValueError("Cannot convert zero vector into a unit vector.")
        
        self.__x /= mag
        self.__y /= mag
        
    
        
    
        
    
