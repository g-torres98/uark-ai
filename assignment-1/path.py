#************************************************
'''
    Path class
    Contains attributes:
        - path: list of nodes (references)
        - cost: total cost of path (add heuristic when using a*)
'''
#************************************************ 

class path():
    def __init__(self, init_path=[]):
        self.path = init_path
        self.cost = 0
    
    # Add node u
    def add_node(self, u):
        self.path.append(u)
        
    # Return head of path (most recently-added node)
    def head(self):
        return self.path[len(self.path)-1]
        
    # Return a new list q from this list
    def copy(self, new_item):
        q = []
        for i in range(len(self.path)-1):
            q.append(self.path[i])
        q.append(new_item)
        return q
