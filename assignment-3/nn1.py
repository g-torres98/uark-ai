#************************************************
# CSCE 4613 Artificial Intelligence Assignment 3
# Neural Network 1--Backpropagation-based XOR Neural Network
# Guadalupe Torres
# Manuel Serna-Aguilera
#************************************************

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------
# Draw the regression line for classification
#------------------------------------------------
def draw(x1, x2):
    ln = plt.plot(x1, x2)
    plt.pause(0.0001) # secs
    ln[0].remove() # remove old line with new to make a cool animation

#------------------------------------------------
# Sigmoid activation function
#------------------------------------------------
def sigmoid(X):
    return 1/(1 + np.exp(-X))

#------------------------------------------------
# Optimize NN parameters
#------------------------------------------------
def train(X, Y, layers, iterations, learning_rate):
    # Store optimized parameters into a dict
    parameters = {}
    
    # Initialize weights (random normal numbers) for each layer
    W1 = np.random.randn(layers[1], layers[0])
    W2 = np.random.randn(layers[2], layers[1])
    
    # Initialize biases to zero, store in a dictionary
    b1 = np.zeros((layers[1], 1))
    b2 = np.zeros((layers[2], 1))
    
    for i in range(0, iterations+1):
        # Forward propagation--calculate linear (affine) transformations Z and post-activation output A
        Z1 = np.dot(W1, X) + b1
        A1 = np.tanh(Z1)
        Z2 = np.dot(W2, A1) + b2
        A2 = sigmoid(Z2)
        
        # Backpropagation
        dZ2 = A2 - Y
        dW2 = np.dot(dZ2, A1.T)/m
        db2 = np.sum(dZ2, axis=1, keepdims=True)/m
        
        dZ1 = np.multiply(np.dot(W2.T, dZ2), 1-np.power(A1, 2))
        dW1 = np.dot(dZ1, X.T)/m
        db1 = np.sum(dZ1, axis=1, keepdims=True)/m
        
        # Update parameters
        W1 = W1 - learning_rate*dW1
        b1 = b1 - learning_rate*db1
        W2 = W2 - learning_rate*dW2
        b2 = b2 - learning_rate*db2
    
    #Return optimized function weights and biases
    parameters["W1"] = W1
    parameters["b1"] = b1
    parameters["W2"] = W2
    parameters["b2"] = b2
    return parameters



#------------------------------------------------
# Make a prediction with a the trained model given input point X
#------------------------------------------------
def predict(X, parameters):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    
    yhat = A2
    yhat = np.squeeze(yhat)
    
    if(yhat >= 0.5):
        prediction = 1
    else:
        prediction = 0
    return prediction



#================================================
# Train model
#================================================
np.random.seed(2)

# Training examples (from truth table) and corresponding correct outputs
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
Y = np.array([[0, 1, 1, 0]])

# Number of training examples
m = X.shape[0]

# Array to hold number of nodes in an n-layered NN with range 0..n
# For this NN, we only have layers 0, 1, 2 for the input, hidden, and output layers respectively
layers = [2, 2, 1]

# Define how many times to iterate over data and learning rate
iterations = 1500
learning_rate = 0.25

# Train the model given the information given (above)
model = train(X, Y, layers, iterations, learning_rate)



#================================================
# With the optimized function, make predictions
#================================================

# Test 2X1 vector to calculate the XOR of its elements. 
# Try (0, 0), (0, 1), (1, 0), (1, 1)
point = np.array([[.25], [.65]])
prediction = predict(point, model)
print("Given ({}, {}).\nPrediction: {}".format(point[0][0], point[1][0], prediction))

#------------------------------------------------
# Label points and show plot
#------------------------------------------------
n_pts = 100
_, ax = plt.subplots(figsize=(4,4))
plt.ylim(0, 1)
plt.xlim(0, 1)

# Starting points to graph
x = 0.0
y = 0.0

while not x > 1.0:
    plt.scatter(x, y)
    x += 0.1
    y += 0.1

#plt.scatter(*np.random.randint(0, high=100, size = (2, n_pts)))

#ax.scatter(top_region[:, 0], top_region[:, 1], color = 'r') # label red
#ax.scatter(bottom_region[:, 0], bottom_region[:, 1], color = 'b') # label blue
#gradient_descent(line_parameters, all_pts, y, 0.06)
plt.show()
