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
    # Take in edges information when making graph for A* procedure, now take in heuristics
    G = graph.graph(use_heuristics=True)
    
    # Add starting node to path
    s = G.get_node(start)
    p = path.path(using_f=True)
    p.add_node(s)
    
    # Add initial path to min-priority queue
    Q = pq.priority_queue()
    Q.append(p)
    
    while not Q.is_empty():
        # Pop path P with lowest cost, subtract
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
            
            del G
            del P
            del Q
            
            print("A*\nNum nodes visited: {}\nNum nodes on path: {}\nDistance (km): {}".format(tot_visited, in_path, distance))
            return
        
        # Explore neighbors, add them to new and distinct lists
        for edge in G.edges[P.head().label]:
            # Only consider unvisited nodes
            if G.get_node(edge.v).color == 'w':
                # Get new path--expand on current list and increase total distance
                new_path = path.path(init_path=P.copy(G.get_node(edge.v)), init_cost=P.cost, init_f=float(P.cost)+float(G.get_node(edge.v).h), using_f=True)
                
                # Add cost so min-queue can account for prospective node heuristic
                new_path.cost += float(edge.dist)
                
                # Append valid path to list of possible paths
                Q.append(new_path)
        
        # Current node is considered visited, color it black
        P.head().color = 'b'
    
    # Return failure
    return None

search('105050228', '105012740')
#search('1', '7')
