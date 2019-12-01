#************************************************
# CSCE 4613 Artificial Intelligence Assignment 3
# Neural Network 1--Backpropagation-based XOR
# Guadalupe Torres
# Manuel Serna-Aguilera
#************************************************

# TODO: we should not use numpy as I think Luu did want us to 
# Use only the scientific lib numpy to help implement the NN
import numpy

'''
Notes:

-Think of a neural network as a large function with many variables. 
-Visually the function is represented as a network with multiple layers (input--first--layer, inner--hidden--layers, and output--classification--layers).
-Each layer depends on weights, so the key is to adjust these weights so that certain layers and certain neurons have more say in the output.

- This NN will learn, given two inputs x1 and x2, the XOR function and output the following outputs for y.

x1 | x2 | y=x1 xor x2
---+----+---
0  | 0  | 0
0  | 1  | 1
1  | 0  | 1
1  | 1  | 0
'''

#------------------------------------------------
# Define activation functions
#------------------------------------------------
def sigmoid(X):
    return 1/(1 + np.exp(-X))

#------------------------------------------------
# Define parameters
#------------------------------------------------
# Weights matrix for each consecutive pair of layers
W0 = []
W1 = []
W = [W0, W1] # list of lists

# Biases matrix
B0 = []
B1 = []
B = [B0, B1] # list of lists

