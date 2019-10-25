#************************************************
'''
    Adjacency-list representation of a graph G.
    Contains:
        * node class
        * edge class
        * graph class
    Graph is undirected as streets (edges between intersections) are two-way.
    
    Note: heuristics file needed to create nodes for graph!
'''
#************************************************

# Sentinel for infinity for unknown distances.
infty = 999999

#================================================
'''
    Node Class
    - represent some node u (some intersection on a map)

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
    def __init__(self, label, color='w', f=None, v=None, pred=None, h=0):
        self.label=label
        self.color = color
        self.d = infty
        self.f = f
        self.pred = pred
        self.h=h
    
    # Print all the info of this node in one line.
    def print(self):
        print("ID: ", self.label)
        print("Color: ", self.color)
        print("Heuristic: ", self.h)
        if self.pred != None:
            print("Predecessor: ", self.pred.label)
        else:
            print("No predecessor.")
        print()



#================================================
'''
    Edge Class 
    - represent weighted edge (u, v) (some two-way street on a map)

    Contains attributes:
        * u: starting node for edge (u, v), integer. Here, id1 = u.
        * v: end node for edge (u, v), integer. Here, id2 = v.
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
        return "(id1: {}, id2: {}, {} km)".format(self.u, self.v, self.dist)



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
'''
#================================================
class graph():
    '''
    Read from edges.txt to get:
        - node objects
        - dict of node objects
        - dict of edge lists
    '''
    def __init__(self, use_heuristics=False):
        self.nodes = {}
        self.edges = {}
        self.n = 0
        
        # Create nodes out of every node found in the heuristics
        h_file = 'test_heuristic.txt'
        #h_file = 'heuristic.txt'
        with open(h_file) as f:
            for line in f:
                node_line = line.split()
                self.nodes[node_line[0]] = node(label=node_line[0], h=node_line[1])
                #self.nodes[node_line[0]].h = node_line[1]
                self.n += 1
                #self.nodes[edge_line[0]] = node(label=edge_line[0])
        
        file_name = 'test_graph.txt' # much smaller test data
        #file_name = 'edges.txt'
        with open(file_name) as f:
            for line in f:
                edge_line = line.split()
                
                # Insert undirected edge (u, v) and (v, u)
                # (u, v)
                if edge_line[0] not in self.edges:
                    self.edges[edge_line[0]] = [edge(u=edge_line[0], v=edge_line[1], dist=edge_line[2])]
                else:
                    self.edges[edge_line[0]].append(edge(u=edge_line[0], v=edge_line[1], dist=edge_line[2]))
                # (v, u)
                if edge_line[1] not in self.edges:
                    self.edges[edge_line[1]] = [edge(u=edge_line[1], v=edge_line[0], dist=edge_line[2])]
                else:
                    self.edges[edge_line[1]].append(edge(u=edge_line[1], v=edge_line[0], dist=edge_line[2]))
    
    # Return reference to node with ID node_id
    def get_node(self, node_id):
        label = '{}'.format(node_id)
        return self.nodes[label]
    
    # Return distance/cost of undirected edge (u, v) (u and v strings)
    def get_dist(self, u, v):
        for i in self.edges[u]:
            if i.v == v:
                return float(i.dist)
    
    # Print current status of nodes
    def list_nodes(self):
        for i in self.nodes:
            self.nodes[i].print()
    
    # Print edge info
    def list_edges(self):
        for i in self.edges:
            for j in self.edges[i]:
                print(j.print())
