#Johnson's algorithm

from gen_graph import *
import time
import fibonacci_heap_mod as fhp

#test_graph = gen_adjacent_matrix( 4 , 7 , -1 , 10 )
#test_graph = np.array([[np.inf , 7      , 3      , np.inf , np.inf ],
#                       [np.inf , np.inf , np.inf , 5      , 3      ], 
#                       [np.inf , 2      , np.inf , np.inf , np.inf ], 
#                       [np.inf , np.inf , 1      , np.inf , np.inf ], 
#                       [np.inf , np.inf , np.inf , 1      , np.inf ] ])

#print test_graph

#def Relax( u , v , w ):
#    if dist(u) > dist(v) + w(u,v)
#        d(v) = d(u) + w(u,v) 

def Bellman_Ford( graph , E , s ):
    v = len(graph)
    dist = np.zeros(v)
    #preV = np.zeros(v)
    dist[s] = 0 
    #for i in preV:
    #    i = np.NaN
    change = True ; 
    # v-1 iterations
    for i in range(v):
        # for each edge
        change = False
        #print dist
        for edge in E:
            if dist[edge[0]] + graph[edge[0]][edge[1]] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + graph[edge[0]][edge[1]]
                change = True 
        if change == False: 
            break 
        '''
        for r in range(v):
            for c in range(v-1):
                if graph[r][c] <= np.inf:
                # Relax
                    if dist[r] + graph[r][c] < dist[c]:
                        dist[c] = dist[r] + graph[r][c]
    #                    preV[c] = r 
        '''
    #check Neg_cycles
    for edge in E:
        if dist[edge[0]] + graph[edge[0]][edge[1]] < dist[edge[1]]:
            print "Graph contains a negative-weight cycle"
            return False    
    '''
    for r in range(v):
        for c in range(v-1):
            if graph[r][c] <= np.inf:
                if dist[r] + graph[r][c] < dist[c]:
                      print "Graph contains a negative-weight cycle"
    '''
    #print " Bellman result \n" , dist
    return dist

def update_graph( graph , E , h ):
    v = len(graph)
    for r in range(v):
        for c in range(v):
            graph[r][c] = graph[r][c] + h[r] - h[c]
 
def extract_min( Q , dist ):
    rest = dist[Q[0]]
    idx = Q[0] 
    for i in Q:
        if dist[i] < rest:
            rest = dist[i]
            idx = i 
    Q.remove(idx)
    return idx

def Dijkstra( graph , s , V ):
    #init
    v = len(graph)
    dist = np.zeros(v)
    #prev = np.zeros(v)
    dist[:] = np.inf
    dist[s] = 0
    #prev[:] = np.NaN
    #S= []
    Entry_list = [ ] 
    #Q_list = range(v)
    Q_FHeap = fhp.Fibonacci_heap() 
    for i in range(v):
        Entry_list = Entry_list + [ Q_FHeap.enqueue( i , dist[i] ) ] 

    #while len(Q_list) > 0:
    while (Q_FHeap) :
        #r_list = extract_min ( Q_list , dist ) 
        r_FHeap = Q_FHeap.dequeue_min()
        #print "r.elem=  " , r_FHeap.m_elem , "  r.pri = ", r_FHeap.m_priority
        #print "r.list=  " , r_list         , " dist[r] = ", dist[r_list]
        #S = S + [ r_list ] 
        #r = r_list
        r = r_FHeap.m_elem
        #S = S + [ r ]
        
        for c in V[r]:
            if dist[r] + graph[r][c] < dist[c]:
                dist[c] = dist[r] + graph[r][c]
                Q_FHeap.decrease_key( Entry_list[c] , dist[c] )
                
        '''
        for c in range(v):
            if graph[r][c] < np.inf:
                if dist[r] + graph[r][c] < dist[c]:
                    dist[c] = dist[r] + graph[r][c]
                    #print Entry_list[c].m_elem , ", ", Entry_list[c].m_priority, ", " , dist[c]
                    Q_FHeap.decrease_key( Entry_list[c] , dist[c] )
    #                prev[c] = r
        ''' 
    return dist 


def Dijkstra_all( graph , V): 
    v = len(graph)
    # for all vertice 
    output = Dijkstra( graph , 0 ,V)
    for i in range(1,v): 
        h = Dijkstra( graph , i , V)
        output = np.vstack([ output , h ])
        #o_prev = np.vstack([ o_prev , prev ])
    return output 

def Johnson( graph , E , V):
    v = len(graph)
    e = len(E)
    node_p = v * [ 0 ]                     # Add nodes
    for i in range(v):
        E = E + [ ( v , i ) ]
    graph = np.vstack([ graph , node_p] )  # Add the edges
    #print "add node_p \n" , graph
    start = time.time()
    h = Bellman_Ford ( graph , E , v )     # Bellman-Ford + Detect Negative Cycle
    end = time.time()
    print " Bellman_Ford -> runtime = " , end - start
    try:
        if (bool(h) == False):
            return False
    except:
        pass
    #print " h = \n" , h
    ud_graph = np.delete( graph , v , 0 )  # Update -> Graph
    #print " delete \n" , graph
    #print "before update \n" , ud_graph
    E = E[:e]
    update_graph ( ud_graph , E , h )
    #print " update \n" , ud_graph
    start = time.time()
    dist = Dijkstra_all( ud_graph , V)
    end = time.time()
    print " Dijkstra_all -> runtime = " , end - start
    #print " dist \n" , dist
    #print " h =  \n" , h 
    update_graph ( dist , E , -h )
    #print "\n"
    return dist
#print Johnson(test_graph) 
