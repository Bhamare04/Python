# import matplotlib.pyplot as plt
# from torchvision import datasets, transforms
# import numpy as np
# #load the CIFAR-10 dataset
# transform = transforms.ToTensor()
# train_dataset = datasets.CIFAR10(
#     root="./data",
#     train=True,
#     download=True,
#     transform=transform
# )

# #visualize some sample images from the dataset
# fig,axes = plt.subplots(1,5,figsize=(12,3))
# for i in range(5):
#     image,label = train_dataset[i]
#     axes[i].imshow(image.permute(1,2,0))
#     axes[i].axis('off')
#     axes[i].set_title(f"Label: {label}")
# plt.show()

# #display pexel values of the first image
# first_image,label = train_dataset[0][0]
# print("Pixel values of the first image:")
# print(label)
# print("Shape of the first image:", first_image.shape)
# print(first_image)


import tensorflow as tf

from Deep_learning.tensorflow_nn import X_train
#define the model architecture
model = tf.keras.Sequential([

    # Convolution layer
    tf.keras.layers.Conv2D(
        32,
        (3, 3),
        padding="same",
        activation="relu",
        input_shape=(32, 32, 3)
    ),

    # Pooling
    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    # Second convolution
    tf.keras.layers.Conv2D(
        64,
        (3, 3),
        padding="same",
        activation="relu"
    ),

    # Second pooling
    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    # Convert feature maps to vector
    tf.keras.layers.Flatten(),

    # Classification layer
    tf.keras.layers.Dense(
        128,
        activation="relu"
    ),

    # Output layer
    tf.keras.layers.Dense(
        10,
        activation="softmax"
    )
])

#compile the model
model.compile(
    optimier='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

#train the model
# history = model.fit(
#     X_train,
#     y_train,
#     epochs=10,
#     batch_size=64,
#     validation_split=0.1
# )