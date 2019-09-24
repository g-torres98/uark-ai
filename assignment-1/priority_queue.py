'''
    Priority Queue class
    
    Adapted from AI book GitHub repo:
    https://github.com/aimacode/aima-python/blob/master/utils.py
'''

import heapq

class priority_queue:
    """
        A Queue in which the minimum element (as determined by f and order) is returned first.
        Order is 'min', the item with minimum f(x) is
        returned first.
        #Also supports dict-like lookup.
    """

    #def __init__(self, order='min', f=lambda x: x):
    def __init__(self):
        self.heap = []
        #self.f = f

        #if order == 'min':
        #    self.f = f
        #elif order == 'max':  # now item with max f(x)
        #    self.f = lambda x: -f(x)  # will be popped first
        #else:
        #    raise ValueError("order must be either 'min' or 'max'.")
        
    def is_empty(self):
        return len(self.heap) == 0

    """Insert PATH at its correct position according to its cost."""
    #TODO: I want to append the path list itself and maintain the min-priority queue according to p.cost. Perhaps a way to do this is to append the entire list object p to self.heap as an element and when we pop, pop the list object(?)
    
    # Store into heap the tuple (cost, object) and order by cost
    def append(self, path):
        heapq.heappush(self.heap, (path.cost, path))
    '''
    def extend(self, items):
        """Insert each item in items at its correct position."""
        for item in items:
            self.append(item)
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
'''
    def __contains__(self, key):
        """Return True if the key is in PriorityQueue."""
        return any([item == key for _, item in self.heap])
'''
'''
    def __getitem__(self, key):
        """Returns the first value associated with key in PriorityQueue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")
'''
'''
    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

'''
