#************************************************
'''
    Path class
    Contains attributes:
        - path: List of nodes (references)
        - cost: Total cost of path (add heuristic when using a*). Still need to add the new edge's cost, constructor only adds total cost of current path P.
'''
#************************************************ 

class path():
    def __init__(self, init_path=[], init_cost=0):
        self.path = init_path
        self.cost = init_cost
    
    # Add node u
    def add_node(self, u):
        self.path.append(u)
        
    # Return head of path (most recently-added node)
    def head(self):
        return self.path[len(self.path)-1]
        
    # Return a new path q from this list and append new node at the end of q
    def copy(self, new_item):
        q = []
        for i in range(len(self.path)):
            q.append(self.path[i])
        q.append(new_item)
        return q
    
    def print(self):
        for i in self.path:
            print(i.label, ', ')
    
    def __lt__(self, other):
        return self.cost < other.cost
