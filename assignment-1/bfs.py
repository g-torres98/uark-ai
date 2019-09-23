#************************************************
'''
    Breadth-first search.
    Parameters:
        * start: start node ID
        * goal: goal node ID 
    We want to find a path such that some path p={start, ..., goal}.
'''
#************************************************

import graph
import queue

def search(start, goal):
    # Take in edges information when making graph for BFS procedure
    G = graph.graph()
    
    # Begin search at starting node s, initialize values
    s = G.get_node(start)
    s.color = 'g'
    s.d = 0
    
    # Create empty queue Q, immediately insert s and start exploring
    Q = queue.Queue(G.n)
    Q.enqueue(s)
    
    # Keep exploring graph until node with ID "goal" is found.
    while not Q.is_empty():
        u = Q.dequeue()
        
        # Loop through nodes connected to u to make edges (u, v)
        for i in G.edges[u.label]:
            # Get nodes v(i) u connects to
            v = G.nodes[i.v]
            
            # Check color and update if undiscovered. 
            # Also check if updated node is goal node.
            if v.color == 'w':
                v.color = 'g'
                v.d = u.d + 1
                v.pred = u
                Q.enqueue(v)
            
            '''
            Found goal node!
            
            Now, return string:
                Num nodes visited: ?
                Num nodes in path: ?
                Distance (km):     ?
            '''
            if v.label == goal:
                tot_visited = 0
                for i in G.nodes:
                    if G.nodes[i].color == 'g' or G.nodes[i].color == 'b':
                        tot_visited += 1
                in_path = 0
                distance = 0
                j = G.nodes[goal]
                while True:
                    if j.label == start:
                        in_path += 1
                        break
                    else:
                        in_path += 1
                        distance += G.get_dist(j.label, j.pred.label)
                        j = j.pred
                return "BFS\nNum nodes visited: {}\nNum nodes on path: {}\nDistance (km): {}".format(tot_visited, in_path, distance)
        u.color = 'b'
    return None

# Test call, uncomment code below: $ python bfs.py
#print(search('1', '7'))
