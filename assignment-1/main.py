#************************************************
'''
    Assignment 1 Main Program
    
    Purpose: Test BFS, UCS, A* search algorithms on a graph with provided nodes.
    Authors: 
        Manuel Serna-Aguilera
        Guadalupe Torres
    CSCE 4613 Artificial Intelligence
    Dr. Khoa Luu
'''
#************************************************

# Import search methods as modules
import bfs
import ucs
import astar

print(bfs.search('1', '7'))
print()
print(ucs.search('1', '7'))
print()
print(astar.search('1', '7'))
print()
