

# TODO: adapt graph class to take in heuristics input file
# TODO: adapt UCS


#************************************************
'''
    A* Search
    Parameters:
        * start: start node ID
        * goal: goal node ID 
    We want to find a more optimal path (with heuristics) such that some path p={start, ..., goal}.
'''
#************************************************

import graph
import priority_queue as pq
import path

def search(start, goal):
    # Take in edges information when making graph for A* procedure
    G = graph.graph()
    
    # Add starting node to path
    s = G.get_node(start)
    p = path.path()
    p.add_node(s)
    
    # Add initial path to min-priority queue
    Q = pq.priority_queue()
    Q.append(p)
    
    while not Q.is_empty():
        # Pop path P with lowest cost
        P = Q.pop()
        
        '''
        Found goal node!
        
        Now, return string:
            Num nodes visited: ?
            Num nodes in path: ?
            Distance (km):     ?
        '''
        if P.head().label == goal:
            tot_visited = 0
            for i in G.nodes:
                if G.nodes[i].color == 'b':
                    tot_visited += 1
            in_path = len(P.path)
            distance = P.cost
            
            return "A*\nNum nodes visited: {}\nNum nodes on path: {}\nDistance (km): {}".format(tot_visited, in_path, distance)
        
        # Explore neighbors, add them to new and distinct lists
        for edge in G.edges[P.head().label]:
            # Only consider unvisited nodes
            if G.get_node(edge.v).color == 'w':
                # Get new path--expand on current list and increase total distance
                new_path = path.path(init_path=P.copy(G.get_node(edge.v)), init_cost=P.cost)
                new_path.cost += float(edge.dist)
                
                # Append valid path to list of possible paths
                Q.append(new_path)
        
        # Current node is considered visited, color it black
        P.head().color = 'b'
    
    # Return failure
    return None
