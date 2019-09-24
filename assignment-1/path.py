#************************************************
'''
    Path class
    Contains attributes:
        - path: list of nodes (references)
        - cost: total cost of path (add heuristic when using a*)
'''
#************************************************ 

class path():
    def __init__(self):
        self.path = []
        self.cost = 0
    
    # Add node u
    def add_node(self, u):
        self.path.append(u)
        
    # Return head of path (most recently-added node)
    def head(self):
        return self.path[len(self.path)-1]
        
    # Return a new list q from input list p
    def copy(p):
        q = []
        for i in p:
            q.append(p[i])
        return q
