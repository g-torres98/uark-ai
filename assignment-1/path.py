#************************************************
'''
    Path class
    Contains attributes:
        - path: List of nodes (references)
        - cost: Total cost of path (add heuristic when using a*). Still need to add the new edge's cost, constructor only adds total cost of current path P.
        - init_f: get new total cost (actual cost + heuristic value) if A* is being used
        - using_f: boolean flag to dictate whether to compare cost or f=cost+h
'''
#************************************************ 

class path():
    def __init__(self, init_path=[], init_cost=0, init_f=0, using_f=False):
        self.path = init_path
        self.cost = init_cost
        self.f = init_f
        self.using_f=using_f
    
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
        if self.using_f:
            return self.f < other.f
        else:
            return self.cost < other.cost
