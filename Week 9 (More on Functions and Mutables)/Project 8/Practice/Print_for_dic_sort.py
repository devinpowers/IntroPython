





L = [('frogger', '2600', 1981, 'action', 'parker bros.', 2200000.0),
 ('e.t.: the extra terrestrial', '2600', 1981, 'action', 'atari', 1970000.0),
 ('burgertime', '2600', 1981, 'puzzle', 'mattel interactive', 590000.0)]


indicator = 'year'
year = 1981

def display_global_sales_data(L, indicator):
    '''
    
        
        L is the list from get_data_by_colmun
    
    '''
    
    #header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
   # header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
   # Sum of Global sales
   
       
    
    if indicator == 'year':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        
        for row in L:
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(row[0],row[1],row[2],row[3],row[4]))
        
    elif indicator == 'platform':
        
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
        
        for row in L:
            
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(row[0],row[1],row[2],row[3],row[4]))
            
    
    #Sum of Global Sales:
    
    print("\n{:90s}{:<12,.02f}".format('The Sum of Global Sales:', global_sales_sum))
    
    