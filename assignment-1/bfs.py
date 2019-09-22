#************************************************
'''
    Breadth-first search.
    Parameters:
        * start: start node ID
        * goal: goal node ID 
    We want to find a path such that optimal path p={start, ..., goal}.
'''
#************************************************

import graph
import queue

#def bfs(G, start):
def bfs(start, goal):
    G = graph.graph()
    # Get vertex from G.V at label "start"
    #s = G.nodes[start]
    
    # Vertex values already assigned, no need to initialize each vertex
    
    G.list_nodes()
    s = G.get_node(start)
    print('current color of s: ', s.color)
    s.color = 'g'
    print('new color of s: ', s.color)# USING REF/POINTER TO CHANGE ATTRIBUTES WORKS!!!
    #s.color = 'g'
    #s.d = 0
    # s.pred is already NIL (look in vertex class constructor)
    G.list_nodes()
    
    #TODO: make sure n is appriately part of G
    # Create empty queue
    #Q = queue.Queue(G.n)
    
    # Keep exploring each vertex's adjacency list to look for gray vertices.
    #Q.enqueue(s)
    
    # Keep dequeuing vertices and see, in the adj array, which other vertices they are connected to, we refer to each vertice's attributes in the V list.
    '''
    #while not Q.is_empty():
        u = Q.dequeue()
        ## Loop through vertices connected to u to make edges (u, v); we get the v values from the edges list G.adj, and then look at G.V.
        for i in G.adj[u.label]:
            # Get vertex
            v = G.nodes[i.v]
            v.print()
            # Check color
            if v.color == 'w':
                v.color = 'g'
                v.d = u.d + 1
                v.pred = u
                Q.enqueue(v)
        u.color = 'b'
    '''
test_best_route = bfs(1, 7)




##########################
# Keep example use
'''
    Original graph:
    r--s  t--u
    |  | /| /|
    v  w--x--y

    Adapted:
    0--1  2--3
    |  | /| /|
    4  5--6--7
'''
'''
n = 8
G = g.graph(n)
G.insert(0, 1)
G.insert(0, 4)
G.insert(1, 0)
G.insert(1, 5)
G.insert(2, 3)
G.insert(2, 5)
G.insert(2, 6)
G.insert(3, 2)
G.insert(3, 6)
G.insert(3, 7)
G.insert(4, 0)
G.insert(5, 1)
G.insert(5, 2)
G.insert(5, 6)
G.insert(6, 2)
G.insert(6, 3)
G.insert(6, 5)
G.insert(6, 7)
G.insert(7, 3)
G.insert(7, 6)

# Output sample graph
G.print()

# Begin breadth-first search starting at vertex with label 1 (look at ascii figure)
s = 1
bfs(G, s)

print("\n\nUpdated G.V\n************************")
for i in G.nodes:
    i.print()
'''
