''' Display Publisher Data Function '''

def display_publisher_data(pub_list):
    '''
       Display Publisher data
    '''
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Title', 'North America', 'Europe', 'Japan', 'Other', 'Global'))

    sum_of_global = 0
    for element in pub_list:
        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(element[1],element[3],element[4],element[5],element[6], element[7]))
    
        sum_of_global += element[7]

    print("\n{:90s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global))
    
'''Input'''
'''
pub_list =[('atari', 'pac-man', 1982, 7280000.0, 450000.0, 0.0, 80000.0, 7810000.0),
 ('atari', 'asteroids', 1980, 4000000.0, 260000.0, 0.0, 50000.0, 4310000.0),
 ('atari','missile command',1980,2560000.0,170000.0,0.0,30000.0,2760000.0),
 ('atari', 'space invaders', 0, 2360000.0, 140000.0, 0.0, 30000.0, 2530000.0),
 ('atari','e.t.: the extra terrestrial',1981,1840000.0,110000.0,0.0,20000.0,1970000.0)
 ]

'''
'''Output'''
'''

Title                         North America  Europe         Japan          Other          Global         
pac-man                       7,280,000.00   450,000.00     0.00           80,000.00      7,810,000.00   
asteroids                     4,000,000.00   260,000.00     0.00           50,000.00      4,310,000.00   
missile command               2,560,000.00   170,000.00     0.00           30,000.00      2,760,000.00   
space invaders                2,360,000.00   140,000.00     0.00           30,000.00      2,530,000.00   
e.t.: the extra terrestrial   1,840,000.00   110,000.00     0.00           20,000.00      1,970,000.00   

Sum of Global Sales:                                                                      19,380,000.00  
'''
