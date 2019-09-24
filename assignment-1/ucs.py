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
    
    p = path.path() # add starting node to path
    p.add_node(s)
    
    Q = pq.priority_queue()
    Q.append(p) # add path to priority queue
    Q.print()
    
    # Access min-heap: >>> Q.heap &&^$%#^$#$%$%*&^)^&(^%^$
    while not Q.is_empty():
        # Pick (and remove) the path P with lowest cost from Q
        u = Q.pop()
        
        print('label: ', u.head().label)
        #print('path: ', u.path)
        # Reached goal
        if u.head().label == goal:
            return u.path
        
        #for v in 
        #print(u.path)
        #print(u.head())
        
        #print('shortest dist: ', u)
        return 0
    
    
    # put node IDs into prioerity queue (in a list)
    return 0
