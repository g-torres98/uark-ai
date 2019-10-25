'''
    Min-priority Queue class
    
    Adapted from AI book GitHub repo:
    https://github.com/aimacode/aima-python/blob/master/utils.py
'''

import heapq

class priority_queue:
    def __init__(self):
        self.heap = []
        
    def is_empty(self):
        return len(self.heap) == 0

    """Insert PATH at its correct position according to its cost."""
    # Store into heap the tuple (cost, object) and order by cost
    def append(self, path):
        if path.using_f:
            heapq.heappush(self.heap, (path.f, path))
        else:
            heapq.heappush(self.heap, (path.cost, path))
    '''
        Insert each item in items at its correct position.
    '''
    def pop(self):
        """Pop and return the path (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')
    
    def print(self):
        print(self.heap)

    def __len__(self):
        """Return current capacity of PriorityQueue."""
        return len(self.heap)
