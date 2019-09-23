#************************************************
'''
    Uniform-cost search (UCS).
    Parameters:
        * start: start node ID
        * goal: goal node ID 
    We want to find a more optimal path such that some path p={start, ..., goal}.
'''
#************************************************

import graph
import priority_queue as pq

def search(start, goal):
    # Take in edges information when making graph for UCS procedure
    G = graph.graph()
    
    # Initialize min-priority queue with starting node ID (list with single start ID)
    frontier = pq.PriorityQueue()
    
    
    # put node IDs into prioerity queue (in a list)
    return 0
