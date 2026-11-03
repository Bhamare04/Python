import numpy as np
import matplotlib.pyplot as plt

#sigmoid function
def sigmoid(z):
    return 1/(1-np.exp(-z))

    #generate synthetic data
z = np.linspace(-10, 10, 100)
sigmoid_values = sigmoid(z)
plt.plot(z, sigmoid_values)
plt.xlabel('Z')
plt.ylabel('sigmoid(Z)')
plt.title('Sigmoid Function')
plt.show()