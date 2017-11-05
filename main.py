# this is main

from Floyd_Warshall import *
from Johnson import *
from gen_graph import *
import time


graph , E = gen_adjacent_matrix( 100 , 100 , 0 , 10)
#graph = np.array([[ np.NaN,   9.   ,   9.   ,   7.   ],
#                  [  4.   ,  np.NaN,   -9.   ,  np.NaN],
#                  [ -1.   ,  np.NaN,  np.NaN,   0.   ],
#                  [ np.NaN,  np.NaN,  np.NaN,  np.NaN]])

print graph , "\n"
start = time.time()
print Johnson( graph , E )  , "\n"
end = time.time()
print " Johnson -> runtime = " , end - start
start = time.time()
print Floyd_Warshall(graph) , "\n"
end = time.time()
print " Floyd_Warshall -> runtime = " , end - start
