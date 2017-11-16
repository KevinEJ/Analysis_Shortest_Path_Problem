# Function to generate a graph 
import numpy as np
import random

def gen_adjacent_matrix( n_vertice , n_edges , min_w , max_w ):
    assert( n_edges <= n_vertice*n_vertice ) 
    graph = np.zeros((n_vertice,n_vertice))
    #graph[:] = np.NaN
    
    i = 0 
    while i < n_edges :
        idx = random.randint(0, n_vertice*n_vertice-1)
        row = idx / n_vertice
        col = idx % n_vertice
        if graph[row][col] != 1 and row!=col:
            graph[row][col] = 1
            i+=1 
    for r in range(n_vertice):
        for c in range(n_vertice):
            if graph[r][c] == 1 :
                graph[r][c] = random.randint( min_w , max_w )
            else:
                graph[r][c] = np.NaN
    #print graph
    #gen_edgeList
    '''
    graph = np.array ( [[ np.inf , -3.   ,  10.    ,7.],
                        [  np.inf , np.inf,  np.inf , np.inf],
                        [  4.     , np.inf,  np.inf , np.inf],
                        [  np.inf ,  8.   ,  np.inf , np.inf]] ) 
    '''
    E = [] 
    for r in range(n_vertice):
        for c in range(n_vertice):
            if graph[r][c] < np.inf:
                E = E + [ (r,c) ]  
    V = [] 
    for r in range(n_vertice):
        vertex_edge =  []  
        for c in range(n_vertice):
            if graph[r][c] < np.inf:
                vertex_edge = vertex_edge + [ c ]  
        V = V + [ vertex_edge ]
    return graph , E, V

#a = gen_adjacent_matrix( 4 , 7 , -10 , 10)
