#************************************************
'''
    Adjacency-list representation of a graph G.
    Contains:
        * node class
        * edge class
        * adjancecy list class
'''
#************************************************

# Sentinel for infinity for unknown distances.
infty = 999999

#================================================
'''
    Node Class
    - represent some node u

    Contains attributes:
        * label: the number tagged for each node in the graph, these will be integers.
    
        * color: color of node in the graph when search is done, these are treated as single characters, it is white by default. Possible values:
            - 'w': white--node not discovered yet.
            - 'g': grey--node discovered, but may still be connected to undiscovered (w) vertices.
            - 'b': black--nothing left to discover, we are done with the current node.
        
        * d: discovery time for the node. Will be assigned when node is made grey, assigned sentinel value of infinity. Will be an integer.
        
        * f: finish time. Will be assigned when node is assigned color black, null by default.
        
        * pred: predecessor in the optimal path when performing a graph searchs.

    - Usage
        - To access these vertices, create a list V, and that will denote which node is which. How many vertices there are and thus how long V is will be determined by the variable `n` in the graph class constructor.
'''
#================================================
class node():
    def __init__(self, label, color='w', f=None, v=None, pred=None):
        self.label=label
        self.color = color
        self.d = infty
        self.f = f
        self.pred = pred
    
    # Print all the info of this node in one line.
    def print(self):
        print("ID: ", self.label)
        print("Color: ", self.color)
        print("Discovery Time: ", self.d)
        print("Finish Time: ", self.f)
        if self.pred != None:
            print("Predecessor: ", self.pred.label)
        else:
            print("No predecessor.")
        print()



#================================================
'''
    Edge Class
    - represent weighted edge (u, v)

    Contains attributes:
        * u: starting node for edge (u, v), integer.
        * v: end node for edge (u, v), integer.
        * dist: weight/cost/distance of edge, 1 by default, integer.

    * In the graph class, the list adj will be created and will house these objects in it.
'''
#================================================
class edge():
    def __init__(self, u, v, dist=1):
        self.u = u
        self.v = v
        self.dist = dist
    
    # Print edge info
    def print(self):
        return "(id1: {}, id2: {}, {} km)".format(self.v, self.u, self.dist)



#================================================
'''
    Graph Class
    - can decide if using heuristic values or not (for A* search)

    Contains attributes:
        * nodes: dictionary where 
            - key: unique node ID
            - value: node object
        * edges: dictionary where
            - key: starting edge u in edge (u, v)
            - value: dictionary where
                > key: end node v ID
                > value: distance of edge (u, v)
        * n: count of unique nodes
        
        Note: for this assignment, the graph is assumed to be directed.
'''
#================================================
class graph():
    def __init__(self, use_heuristics=False):
        self.nodes = {}
        self.edges = {}
        self.n = 0
        
        '''
        Read from edges.txt to get:
            - node objects
            - dict of node objects
            - dict of edges
        '''
        with open('edges.txt') as f:
            for line in f:
                edge_line = line.split()
                
                # Insert nodes
                if edge_line[0] not in self.nodes:
                    self.nodes[edge_line[0]] = node(label=edge_line[0])
                
                # Insert some edge starting at node with current ID
                if edge_line[0] not in self.edges:
                    self.edges[edge_line[0]] = [edge(u=edge_line[0], v=edge_line[1], dist=edge_line[2])]
                else:
                    self.edges[edge_line[0]].append(edge(u=edge_line[0], v=edge_line[1], dist=edge_line[2]))
            
        
        # Insert edges one node ID at a time as a dict for every unique ID
        '''
        for node_id in self.nodes:
            try:
                self.edges[node_id]
            except KeyError:
                self.edges.update({edge[1]: edge[2]})
                print(self.edges)
        '''
        #example manual creation of dict tg = {12: 10}
        for i in self.edges:
            print(i)
            for j in self.edges[i]:
                print('\t', i, ' ', j.print())
        
        
        #text = open('edges.txt', 'r')
        #text_str = text.read()
        #print(text_str)
        
        
        
        
        
        
        
        self.n = 0
        
        # Crate set of vertices V
        self.nodes = []
        for i in range(self.n):
            self.nodes.append(node(label=i))

        # Create list of edges adj for each node
        self.adj = []
        for i in range(self.n):
            self.adj.append([])

    # Print the adjancency list with the option to show weights.
    def print(self):
        print("Printing adjacency list.")
        for i in range(self.n):
            edges = self.adj[i]
            paths = str(i)
            for j in range(len(edges)):
                paths += "->{}".format(edges[j].print())
            print(paths)
        print()

    # Insert edge (u, v) with weight (if directed) into adj.
    def insert(self, u, v, w=1):
        self.adj[u].append(edge(u, v, w))

    # Remove edge (u, v) from graph.
    # Look at label/ID of u, look at all vertices that make edges (u, v).
    def remove(self, u, v):
        edges = self.adj[u]
        for i in range(len(edges)):
            if self.adj[u][i].v == v:
                print('Found at index {}! {}'.format(i, self.adj[u][i].get(False)))
                del self.adj[u][i]
                break








g = graph()

