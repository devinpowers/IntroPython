

# Sorting Dictionaries

from operator import itemgetter


D = {'searchResult' : [{'resultType' : 'station',
                        'ranking' : 0.5},
                
                       {'resultType' : 'station',
                        'ranking' : 0.35},
                       
                       {'resultType' : 'station',
                        'ranking' : 0.40}
                       
                       ]}

            
            
D["searchResult"].sort(key=itemgetter("ranking"),reverse=True)

#print(D)

d = { 'a1': ['g',6],
      'a2': ['e',2],
      'a3': ['h',3],
      'a4': ['s',2],
      'a5': ['j',9],
      'a6': ['y',7] 
      }


L = sorted(d, key=lambda k: d[k][1], reverse = True)

L2 = sorted(d, key=lambda k: d[k][0], reverse = True)

print(L)

print(L2)