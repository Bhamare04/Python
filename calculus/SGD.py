#perform SGD on a simple linear regression model
import numpy as np
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

#add bias term to the input data
x_b = np.c_[np.ones((100, 1)), x]

#sgd function
def sgd(x, y, learning_rate=0.01, n_epochs=50, batch_size=20):
    m = len(y)
    for epoch in range(n_epochs):
        for i in range(m):
            random_index = np.random.randint(m)
            x1 = x_b[random_index:random_index+1]
            y1 = y[random_index:random_index+1]
            gradients = 2 * x1.T.dot(x1.dot(theta) - y1)
            theta = theta - learning_rate * gradients  

    return theta
theta = np.random.randn(2, 1)
learning_rate = 0.01
n_epochs = 50

#perform SGD
theta = sgd(x_b, y, learning_rate, n_epochs)
print("optimal parameters:", theta)