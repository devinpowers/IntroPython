
"""
Display Genre Data Function
"""

def display_genre_data(genre_list):
    '''
        Display Genre Data
    '''
    
    print( "{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global'))
    
    sum_of_global = 0
  
    for element in genre_list:
    
        print("{:15s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(element[0],element[2],element[3],element[4], element[5], element[6]))

        sum_of_global += element[6]
        
    print("\n{:75s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global))
    
    
''' Input '''

'''

genre_list= [('action', 2, 3900000.0, 230000.0, 0.0, 40000.0, 4170000.0),
 ('puzzle', 1, 550000.0, 30000.0, 0.0, 10000.0, 590000.0)]


'''

''' Output '''

'''

Genre          North America  Europe         Japan          Other          Global         
action         3,900,000.00   230,000.00     0.00           40,000.00      4,170,000.00   
puzzle         550,000.00     30,000.00      0.00           10,000.00      590,000.00     

Sum of Global Sales:                                                       4,760,000.00
'''
