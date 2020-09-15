#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 12: More on Classes

"""




def special_sum(a,b):
    ' ' ' sum two ints or convert params to ints and add. return 0 if conversion fails '''
    
    if type(a)==int and type(b)==int:
        result = a + b
    else:
        try:
            result = int(a) + int(b)
            
        except ValueError: result = 0
    
    return result


class MyClass(object):
    
    def init (self, param1=0):
        '''constructor , sets attribute value to param1 , default is 0'''
        print('in constructor')
        self.value = param1
    
    def __str__(self):
        ''' Convert val attribute to string. '''
        print('in str')
        return 'Val is: {}'. format(str(self.value))
    
    def __add__(self, param2):
        '''Perform addition with param2, a MyClass instance.
        Return a new MyClass insrance with sum as value attribute'''
        
        print('in add')
        result = self.value + param2.value
        return MyClass(result)
        
        
        
'''Building the Rational Number Class'''   

def gcd(bigger, smaller):
    
    """Calculate the greatest common divisor of two positive integers."""
    print('in gcd)')
    if not bigger > smaller: # swap if necessary so bigger > smaller
        bigger, smaller = smaller, bigger
    while smaller != 0:                                 # 1. if smaller == 0, halt
        remainder = bigger % smaller                   # 2. find remainder
      #  print('calculation, big:{}, small:{}, rem:{}'.\
    #         format(bigger, smaller, remainder)) # debugging
        bigger, smaller = smaller, remainder #           3. reapply
    return bigger

def lcm (a,b):
    
    ''' Calculate the lowest common multiple of two positive integers. '''
    print('in lcm')
    return (a*b)// gcd(a,b) # Equation 12.1, // ensures an int is returned
    

   

class Rational(object):
    
    """ Rational with numerator and denominator. Denominator parameter defaults to 1"""
    
    def __init__ (self,numer,denom=1):
        print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__ (self):
        """ String representation for printing""" 
        print('in str')
        return str(self.numer)+'/'+str(self.denom)
    
    def __repr__ (self):
        """ Used in interpreter. Call str for now """ 
        print('in repr')
        return self.__str__()
    
    def add (self, param):
        
        """ Add two Rationals . Allows int as a parameter""" 
        print('in add')
        if type(param) == int: # convert ints to Rationals
            param = Rational(param)
        if type(param) == Rational:
            # find a common denominator (lcm)
            the_lcm = lcm(self.denom, param.denom)
            # multiply each by the lcm , then add
            numerator_sum = (the_lcm * self.numer/self.denom) + \
                (the_lcm * param.numer/param.denom)
            return Rational(int(numerator_sum),the_lcm)
        else:
            print('wrong type') # problem : some type we cannot handle 
            raise(TypeError)
            

    def __add__(self, param_Rational):
        
        """ Add two Rationals""" 
        print('in add')
        # find a common denominator (lcm)
        the_lcm = lcm(self.denom, param_Rational.denom)
        
        # multiply each by the lcm , then add
        numerator_sum = (the_lcm * self.numer/self.denom) + \
                        (the_lcm * param_Rational.numer/param_Rational.denom)
        return Rational(int(numerator_sum), the_lcm)
    
    def __sub__(self, param_Rational):
        """ Subtract two Rationals"""
        print('in sub')
        # subtraction is the same but with '−' instead of '+'
        the_lcm = lcm(self.denom, param_Rational.denom)
        numerator_diff = (the_lcm * self.numer/self.denom) - (the_lcm * param_Rational.numer/param_Rational.denom)
        
        return Rational(int(numerator_diff), the_lcm)
    
    
def reduce_rational(self):
    """Return the reduced fractional value as a Rational"""
    print('in reduce')
    # find the gcd then divide numerator and denominator by gcd
    the_gcd = gcd(self.numer, self.denom)
    return Rational(self.numer // the_gcd, self.denom//the_gcd)

def __eq__(self, param_Rational):
    '''Compare two Rationals for equality, return Boolean'''
    print('in eq')
    # Reduce both; then check that numerator and denominators are equal
    reduced_self = self.reduce_rational()
    reduced_param = param_Rational.reduce_rational()
    return reduced_self.numer == reduced_param.numer and\
        reduced_self.denom == reduced_param.denom
        
    

    
    
    
def __radd__ (self, param):
    '''Add two Rationals (reversed) '''
    # mapping is reversed: if "1 + x", x maps to slef, and 1 maps to f
    print('in radd')
    # mapping is already reversed so self will be Rational; call __add__
    return self.__add__(param)
    


    
    
    