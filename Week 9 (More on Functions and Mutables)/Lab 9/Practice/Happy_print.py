
from operator import itemgetter

dictionary = {'Los_Angeles': {'Lakers': ['James', 'Davis', 'Johnson', 'Bryant'],
                     'Clippers': ['George', 'Paul', 'Griffin'],
                     'Sparks': ['Leslie', 'Parker']},
     'Detroit': {'Pistons': ['Wallace', 'Isiah', 'Billups', 'Rodman']},
     'New_York': {'Knicks': ['Frazier', 'Ewing', 'Starks', 'Reed'],
                  'Liberty': ['Ionescu', 'Nurse', 'Xu', 'Durr']},
     'Miami': {'Heat': ['Wade', 'Butler', 'Herro']},
     'Chicago': {'Bulls': ['Pippen', 'Jordan', 'Rose', 'Armstrong'],
                 'Sky': ['Dolson']}}



sorted_cities = sorted(dictionary)

for city in sorted_cities:
    
    print("{:>10s} --> ".format(city),end = '')
    print()
    
    
  
