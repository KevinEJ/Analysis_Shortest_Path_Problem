# Floyd_Warshall Algo

from gen_graph import *

#test_graph = gen_adjacent_matrix( 4 , 7 , -1 , 10 )
test_graph = np.array([[np.inf , 7      , 3      , np.inf , np.inf ],
                       [np.inf , np.inf , np.inf , 5      , 3      ], 
                       [np.inf , 2      , np.inf , np.inf , np.inf ], 
                       [np.inf , np.inf , 1      , np.inf , np.inf ], 
                       [np.inf , np.inf , np.inf , 1      , np.inf ] ])

#print test_graph


def Floyd_Warshall( graph ):
    v = graph[0].size
    #print v
    dist = np.zeros( (v,v,)) 
    dist[:] = np.inf
    #print dist
    
    for r in range( v ):
        for c in range( v ):
            if graph[r][c] < np.inf:
                dist[r][c] = graph[r][c]
    for i in range( v ):
        dist[i][i] = 0 
    #'''
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j] : 
                    dist[i][j] = dist[i][k] + dist[k][j]
    #'''
    for i in range(v):
        if dist[i][i] < 0:
            print "Graph contains a negative-weight cycle"
    return dist 


#print Floyd_Warshall(test_graph)
