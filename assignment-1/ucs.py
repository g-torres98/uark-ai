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
    #s.color = 'g'
    #s.d = 0
    
    p = path.path() # add starting node to path
    p.add_node(s)
    
    Q = pq.priority_queue()
    Q.append(p) # add path to priority queue
    Q.print()
    
    # Access min-heap: >>> Q.heap &&^$%#^$#$%$%*&^)^&(^%^$
    while not Q.is_empty():
        # Pick (and remove) the path P with lowest cost from Q
        P = Q.pop()
        
        print('popped P: ', P.path, ' cost=', P.cost, ' label of current head: ', P.head().label)
        #print('path: ', P.path)
        
        # Reached goal
        if P.head().label == goal:
            print('UCS reached goal!')
            return P.path
        
        # Explore neighbors, add them to new and distinct lists
        for edge in G.edges[P.head().label]:
            if P.head().color == 'w':
                #TODO: consider unvisited nodes only (mark either w or b--visited)
                
                #print(edge.v, ' ', edge.dist)
                print('current edge from head: ', edge.v, ' cost=', edge.dist)
                
                # Get node ref at end of edge
                
                # TODO: check that this matches the data type that the path class constructor should take in (it takes in a list)
                new_path = path.path(init_path=P.copy(G.get_node(edge.v)))
                new_path.cost += float(edge.dist)
                
                print('new path: ', new_path.path, ' with head=', new_path.head().label, ' and path cost=', new_path.cost)
                print()
                
                # Append valid path to list
                Q.append(new_path)
            else:
                print('node {} already visited'.format(P.head().label))
        # Mark current node as visited--color black
        P.head().color = 'b'
        print('--------------')
    
    # Return failure
    return None
