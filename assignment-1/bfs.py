#************************************************
'''
    Breadth-first search.
    
    
'''
#************************************************

import graph as g
import queue

#------------------------------------------------
'''
    Breadth-first search.
    Parameters:
        G: graph with vertices and adjacency list.
        s: starting vertex (vertex object).
'''
#------------------------------------------------
def bfs(G, start):
    # Get vertex from G.V at label "start"
    s = G.nodes[start]
    
    # Vertex values already assigned, no need to initialize each vertex
    
    s.color = 'g'
    s.d = 0
    # s.pred is already NIL (look in vertex class constructor)
    
    # Create empty queue
    Q = queue.Queue(G.n)
    
    # Keep exploring each vertex's adjacency list to look for gray vertices.
    Q.enqueue(s)
    
    # Keep dequeuing vertices and see, in the adj array, which other vertices they are connected to, we refer to each vertice's attributes in the V list.
    while not Q.is_empty():
        u = Q.dequeue()
        
        # Loop through vertices connected to u to make edges (u, v); we get the v values from the edges list G.adj, and then look at G.V.
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
