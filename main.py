# this is main

from Floyd_Warshall import *
from Johnson import *
from gen_graph import *
import time
import sys
import pdb
import numpy as np
#if len(sys.argv) != 2:
assert(len(sys.argv)==3)

n_v = int(sys.argv[1])
n_e = int(sys.argv[2])

graph = gen_adjacent_matrix( n_v , n_e , 0 , 10)
E = gen_E(graph)
V = gen_V(graph)
DL_std = np.std(getDegreeList(V))
num_SCC = get_num_CC(graph)
print "STD = " ,  DL_std , " num_SCC =" , num_SCC

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

try:
    if (bool(dist_1) == False):
        print "NegCycle in Johnson"
except:
    pass
try:
    if( bool(dist_2) == False): 
        print "NegCycle in Floyd_warshall"
except:
    pass

try:
    for r in range(n_v):
        for c in range(n_v):
            if r!=c and dist_1[r][c] != dist_2[r][c]:
                print "r = " , r , " c = " , c , "dist_1 = " , dist_1[r][c] , "dist_2" , dist_2[r][c]
                print "Error!!!!!!!!!!!!!!!"
except:
    pass


Output = open('my_new_output_std_SCC.csv' , 'w')
for i in range(3600):
    graph = gen_adjacent_matrix( n_v , n_e , 0 , 10)
    E = gen_E(graph)
    V = gen_V(graph)
    DL_std = np.std(getDegreeList(V))
    num_SCC = get_num_CC(graph)
    print "STD = " ,  DL_std , " num_SCC =" , num_SCC
    # John
    start = time.time()
    Johnson( graph , E , V)  , "\n"
    end = time.time()
    time_John = end - start 
    print " Johnson -> runtime = " , end - start
    
    #Floyd
    start = time.time()
    Floyd_Warshall(graph) , "\n"
    end = time.time()
    time_Floyd = end - start 
    print " Floyd_Warshall -> runtime = " , end - start
 
    Output.write(str(n_v))
    Output.write(',')
    Output.write(str(n_e))
    Output.write(',')
    Output.write(str(DL_std))
    Output.write(',')
    Output.write(str(num_SCC))
    Output.write(',')
    Output.write(str(time_John))
    Output.write(',')
    Output.write(str(time_Floyd))
    Output.write('\n')
Output.close()
'''
#print graph
#print dist_1
#print dist_2
J = np.zeros((41,11))
F = np.zeros((41,11))

for v in range(1,1):
    for e in range(1 , 10):
        print 'v = ', v , ' , e = ' , e  
        print 'v = ', v*5 , ' , e = ' , (25*v*v-v)/10*e  
        count = 0 
        J[v][e] = 0
        F[v][e] = 0
        while( J[v][e] < 1 or F[v][e] < 1):
        #while( count == 0 ):
            graph , E , V= gen_adjacent_matrix( v*5 , (25*v*v-v)/10*e , 0 , 10)
            # John
            start = time.time()
            Johnson( graph , E , V)  , "\n"
            end = time.time()
            J[v][e] += end - start 
            print " Johnson -> runtime = " , end - start
        
            #Floyd
            start = time.time()
            Floyd_Warshall(graph) , "\n"
            end = time.time()
            F[v][e] += end - start 
            print " Floyd_Warshall -> runtime = " , end - start
            count = count + 1
            #print 'J[',v,'][',e,'] = ' , J[v][e] 
            #print 'F[',v,'][',e,'] = ' , F[v][e] 
        J[v][e] = J[v][e] / count 
        F[v][e] = F[v][e] / count
        #print J
        #print F
        print 'J[',v,'][',e,'] = ' , J[v][e] 
        print 'F[',v,'][',e,'] = ' , F[v][e] 

#print J
#print F
Output = open('my_new_output.csv' , 'w')

##pdb.set_trace()
for v in J:
    for e in v:
        Output.write(str(e))
        Output.write(',')
    Output.write('\n')
#print J
Output.write('\n')
Output.write('\n')
Output.write('\n')
for v in F:
    for e in v:
        Output.write(str(e))
        Output.write(',')
    Output.write('\n')
#print F
'''


