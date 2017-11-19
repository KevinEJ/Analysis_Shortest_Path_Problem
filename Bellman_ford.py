from gen_graph import *
import time

def Bellman_Ford( graph , E , s ):
    v = len(graph)
    dist = np.zeros(v)
    dist[s] = 0 
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
        
    #check Neg_cycles
    for edge in E:
        if dist[edge[0]] + graph[edge[0]][edge[1]] < dist[edge[1]]:
            return False    
    #print " Bellman result \n" , dist
    return True


