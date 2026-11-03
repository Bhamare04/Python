import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def tanh(x):
    return np.tanh(x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x, axis=0, keepdims=True)


#forward pass function
def forward_pass(x,bias,weights,activation_function):
    z = np.dot(weights,x) + bias
    a = activation_function(z)
    return a

#example usage
x = np.array([0.5, 0.2, 0.1])
weights = np.array([[0.1, 0.2, 0.3],[0.4, 0.5, 0.6],[0.7, 0.8, 0.9]])
bias = np.array([0.1, 0.2, 0.3])

#forward pass using sigmoid activation function
output_sigmoid = forward_pass(x,bias,weights,sigmoid)
output_relu = forward_pass(x,bias,weights,relu)
output_tanh = forward_pass(x,bias,weights,tanh)
output_softmax = forward_pass(x,bias,weights,softmax)

print(f"Output using sigmoid activation function: {output_sigmoid}")
print(f"Output using relu activation function: {output_relu}")
print(f"Output using tanh activation function: {output_tanh}")
print(f"Output using softmax activation function: {output_softmax}")


z = np.linspace(-10,10,100)

#plot activation functions
plt.figure(figsize=(10,8))
plt.plot(z,sigmoid(z),label='Sigmoid',color='blue')
plt.plot(z,relu(z),label='ReLU',color='red')
plt.plot(z,tanh(z),label='Tanh',color='green')
plt.plot(z,softmax(z),label='Softmax',color='orange')

plt.title('Activation Functions')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()
plt.show()