"""
Sorting Dictionaries

@author: devinpowers
"""


from operator import itemgetter

d = {'Lakers': ['James', 23],
     'Clippers':['Paul', 3],
     'Pistons': ['Billups', 1],
     'Miami': ['Wade', 3],
     'Chicago':['Jordan',23]
     }
     
                  


sort_d = sorted(d, key=itemgetter(0))




