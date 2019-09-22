#************************************************
'''
    Assignment 1 Main Program
    
    Purpose: Test BFS, UCS, A* search algorithms on a graph with provided nodes.
    Author: Manuel Serna-Aguilera
    CSCE 4613 Artificial Intelligence
    Dr. Khoa Luu
'''
#************************************************

#TODO: import graph module when done with that

#================================================
#Create list out of raw text file.
#================================================
def preprocess_edges(edges_text):
    '''
    edges_list = [] # will contain lists containing contents of each line
    for i in range(len(edges_text)):
        #edges_list.append(i.split())
        print(edges_text[i])
    return edges_list
    '''


#================================================
# Get n--length of vertex set V in G.
#================================================
'''
def get_n(edges_list):
    n = 0
    
    return n
'''

#TODO: after checking that adj list implementation works, work on adding txt file info in this file and testing it in bfs
'''
Read graph information.
    - col 1 OR [0]: node 1
    - col 2 OR [1]: node 2
    - col 3 OR [2]: distance (km)
'''
#edges_file_name = 'edges.txt'

'''
raw_text = open(file_name, 'r')
edges_text = raw_text.read()

edges_text = edges_text.split()
print(edges_text)
'''




# Convert each entry in each line into an element of a list (create list of lists 3 long)
#edges_list = preprocess(edges_text)


# Get n (count how many unique nodes there are)
#n = get_n(edges_list)



#TODO: modify bfs to display the path along with the total km traveled 
#TODO: implement ucs search
#TODO: read heuristic values, and implement a* search
