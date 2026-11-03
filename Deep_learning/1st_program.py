from tensorflow.keras.datasets import mnist,cifar10
import tensorflow as tf
import torch 
import torch.nn as nn

import matplotlib.pyplot as plt

#load MNIst dataset
(x_train,y_train),(x_test,y_test) = mnist.load_data()
#print(f"MNIST dataset loaded: x_train shape: {x_train.shape}, y_train shape: {y_train.shape}, x_test shape: {x_test.shape}, y_test shape: {y_test.shape}")


#load  cifer10 dataset 
(x_train_cifar10,y_train_cifar10),(x_test_cifar10,y_test_cifar10) = cifar10.load_data()
#print(f"CIFAR-10 dataset loaded: x_train shape: {x_train_cifar10.shape}, y_train shape: {y_train_cifar10.shape}, x_test shape: {x_test_cifar10.shape}, y_test shape: {y_test_cifar10.shape}")



layer = tf.keras.layers.Dense(units=10,activation='relu')

print(f"Layer created: {layer}")
#define a basic dense layer unsing pytorch
layer1 = nn.Linear(in_features=342,out_features=3)
print(f"Layer created: {layer1}")

#visualize the first 10 images of the MNIST dataset
plt.imshow(x_train[0],cmap='gray')
plt.title(f"Label: {y_train[3]}")   
plt.show()

#visualize the first 10 images of the CIFAR-10 dataset
plt.imshow(x_train_cifar10[1])
plt.title(f"Label: {y_train_cifar10[0]}")
plt.show()