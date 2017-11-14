# this is main

from Floyd_Warshall import *
from Johnson import *
from gen_graph import *
import time
import sys

#if len(sys.argv) != 2:
assert(len(sys.argv)==3)

n_v = int(sys.argv[1])
n_e = int(sys.argv[2])

graph , E , V = gen_adjacent_matrix( n_v , n_e , 0 , 10)
#graph = np.array([[ np.NaN,   9.   ,   9.   ,   7.   ],
#                  [  4.   ,  np.NaN,   -9.   ,  np.NaN],
#                  [ -1.   ,  np.NaN,  np.NaN,   0.   ],
#                  [ np.NaN,  np.NaN,  np.NaN,  np.NaN]])

#print graph , "\n"
start = time.time()
#print Johnson( graph , E )  , "\n"
dist_1 = Johnson( graph , E , V)
end = time.time()
print " Johnson -> runtime = " , end - start
start = time.time()
#print Floyd_Warshall(graph) , "\n"
dist_2 = Floyd_Warshall(graph)
end = time.time()
print " Floyd_Warshall -> runtime = " , end - start

for r in range(n_v):
    for c in range(n_v):
        if r!=c and dist_1[r][c] != dist_2[r][c]:
            print "r = " , r , " c = " , c , "dist_1 = " , dist_1[r][c] , "dist_2" , dist_2[r][c]
            print "Error!!!!!!!!!!!!!!!"

J = 100*[0]
F = 100*[0]
for i in range(0):
    for e in range(0,0,0):
        print i , ":" , e
        graph , E , V= gen_adjacent_matrix( 50 , e , 0 , 10)
        e = e/50
        # John
        start = time.time()
        Johnson( graph , E , V)  , "\n"
        end = time.time()
        J[e] += end - start 
        print " Johnson -> runtime = " , end - start
        
        #Floyd
        start = time.time()
        Floyd_Warshall(graph) , "\n"
        end = time.time()
        F[e] += end - start 
        print " Floyd_Warshall -> runtime = " , end - start

Output = open('my_output.csv' , 'w')
for i in J:
    Output.write(str(i))
    Output.write(",")
#print J
Output.write("\n")
for i in F:
    Output.write(str(i))
    Output.write(",")
#print F
    
