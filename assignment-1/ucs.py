#************************************************
'''
    Uniform-cost search (UCS).
    Parameters:
        * start: start node ID
        * goal: goal node ID 
    We want to find a more optimal path such that some path p={start, ..., goal}.
'''
#************************************************

import graph
import priority_queue as pq
import path

def search(start, goal):
    # Take in edges information when making graph for UCS procedure
    G = graph.graph()
    
    # Initialize min-priority queue with starting node ID
    s = G.get_node(start)
    s.color = 'g'
    s.d = 0
    
    p = path.path()
    p.add_node(s)
    
    Q = pq.priority_queue()
    Q.append(p)
    Q.print()
    
    # Access min-heap: >>> Q.heap &&^$%#^$#$%$%*&^)^&(^%^$%$%#@!@$#%
    while not Q.is_empty():
        u = Q.pop()
        print('u: ', u)
        
        #print('shortest dist: ', u)
        return 0
    
    
    # put node IDs into prioerity queue (in a list)
    return 0
