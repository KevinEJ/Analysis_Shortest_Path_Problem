# Function to generate a graph 
import numpy as np
import random


def gen_E( graph):
    n_vertice = len(graph)
    E = [] 
    for r in range(n_vertice):
        for c in range(n_vertice):
            if graph[r][c] < np.inf:
                E = E + [ (r,c) ]  
    return E  

def gen_V( graph ):
    n_vertice = len(graph)
    V = [] 
    for r in range(n_vertice):
        vertex_edge =  []  
        for c in range(n_vertice):
            if graph[r][c] < np.inf:
                vertex_edge = vertex_edge + [ c ]  
        V = V + [ vertex_edge ]
    return V

def gen_adjacent_matrix( n_vertice , n_edges , min_w , max_w ):
    assert( n_edges <= n_vertice*n_vertice ) 
    graph = np.zeros((n_vertice,n_vertice))
    
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
    return graph

def gen_test_graph():
    graph = np.array ( [[ np.inf , -3.   ,  10.    ,7.],
                        [  np.inf , np.inf,  np.inf , np.inf],
                        [  4.     , np.inf,  np.inf , np.inf],
                        [  np.inf ,  8.   ,  np.inf , np.inf]] ) 
    return graph


def getDegreeList(V):
    DegreeList = []
    for v in V:
        DegreeList = DegreeList + [ len(v) ] 
    return np.array(DegreeList)

def Reverse_G(graph):
    n_vertice = len(graph)
    R_graph = np.zeros((n_vertice,n_vertice))
    for r in range(n_vertice):
        for c in range(n_vertice):
            R_graph[c][r] = graph[r][c] 
    return R_graph
finish = 1 
def DFS( graph , v , mark ):
    global finish
    n_vertice = len(graph)
    mark[v] = 1 ;
    for i in range(n_vertice):
        if( graph[v][i] < np.inf and mark[i] == 0):
            DFS( graph , i , mark  )
    mark[v] = finish  
    finish = finish + 1 

def get_num_CC(graph):
    n_vertice = len(graph)
    R_graph = Reverse_G ( graph )
    mark = np.zeros(n_vertice)
    finish = 1 
    for v in range(n_vertice):
        if( mark[v] == 0  ): 
            DFS( R_graph , v , mark )
    #print mark
    finish = 1 
    count = 0 
    n_mark = np.zeros(n_vertice)
    for i in range(n_vertice, 0 , -1):
        for v in range(n_vertice):
            #print "i = " , i  , " v = " , v , "   mark ->  " , mark[v]
            if ( mark[v] == i and n_mark[v] == 0 ):
                #print "DFS -> v " , v
                DFS( graph , v , n_mark )
                count = count + 1
    #print n_mark
    return count 
#a = gen_adjacent_matrix( 4 , 7 , -10 , 10)
