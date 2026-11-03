# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt


# # ============================================================
# # 1. LOAD CIFAR-10 DATASET
# # ============================================================

# (X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()

# print("Training data shape:", X_train.shape)
# print("Training labels shape:", y_train.shape)

# print("Testing data shape:", X_test.shape)
# print("Testing labels shape:", y_test.shape)


# # ============================================================
# # 2. DEFINE CLASS NAMES
# # ============================================================

# class_names = [
#     "airplane",
#     "automobile",
#     "bird",
#     "cat",
#     "deer",
#     "dog",
#     "frog",
#     "horse",
#     "ship",
#     "truck"
# ]


# # ============================================================
# # 3. DISPLAY ONE IMAGE
# # ============================================================

# plt.imshow(X_train[0])
# plt.title(class_names[y_train[0][0]])
# plt.axis("off")
# plt.show()


# # ============================================================
# # 4. NORMALIZE PIXEL VALUES
# # ============================================================

# X_train = X_train / 255.0
# X_test = X_test / 255.0

# print("Minimum pixel value:", X_train.min())
# print("Maximum pixel value:", X_train.max())


# # ============================================================
# # 5. BUILD CNN MODEL
# # ============================================================

# model = tf.keras.Sequential([

#     # Input image: 32 x 32 x 3
#     tf.keras.layers.Conv2D(
#         32,
#         (3, 3),
#         activation="relu",
#         input_shape=(32, 32, 3)
#     ),

#     # Reduce image size
#     tf.keras.layers.MaxPooling2D((2, 2)),

#     # Second convolution layer
#     tf.keras.layers.Conv2D(
#         64,
#         (3, 3),
#         activation="relu"
#     ),

#     # Reduce image size again
#     tf.keras.layers.MaxPooling2D((2, 2)),

#     # Convert feature maps into a vector
#     tf.keras.layers.Flatten(),

#     # Fully connected layer
#     tf.keras.layers.Dense(
#         128,
#         activation="relu"
#     ),

#     # Output layer: 10 classes
#     tf.keras.layers.Dense(
#         10,
#         activation="softmax"
#     )
# ])


# # ============================================================
# # 6. DISPLAY MODEL ARCHITECTURE
# # ============================================================

# model.summary()


# # ============================================================
# # 7. COMPILE MODEL
# # ============================================================

# model.compile(
#     optimizer="adam",
#     loss="sparse_categorical_crossentropy",
#     metrics=["accuracy"]
# )


# # ============================================================
# # 8. TRAIN MODEL
# # ============================================================

# history = model.fit(
#     X_train,
#     y_train,
#     epochs=10,
#     batch_size=64,
#     validation_split=0.1
# )


# # ============================================================
# # 9. EVALUATE MODEL
# # ============================================================

# test_loss, test_accuracy = model.evaluate(
#     X_test,
#     y_test
# )

# print("Test Loss:", test_loss)
# print("Test Accuracy:", test_accuracy)


# # ============================================================
# # 10. SAVE MODEL
# # ============================================================

# model.save("cifar10_model.keras")

# print("Model saved successfully!")


# # ============================================================
# # 11. MAKE PREDICTION
# # ============================================================

# predictions = model.predict(X_test)

# predicted_class = np.argmax(predictions[0])
# actual_class = y_test[0][0]

# print("Predicted:", class_names[predicted_class])
# print("Actual:", class_names[actual_class])


# # ============================================================
# # 12. DISPLAY TEST IMAGE WITH PREDICTION
# # ============================================================

# plt.imshow(X_test[0])

# plt.title(
#     "Predicted: " + class_names[predicted_class]
#     + "\nActual: " + class_names[actual_class]
# )

# plt.axis("off")
# plt.show()

import torch
from torchvision import datasets, transforms

transform = transforms.ToTensor()

#load training dataset
train_dataset = datasets.CIFAR10(
    root="./data",
    train = True,
    download = True,
    transform = transform
)

#load testing dataset
test_dataset = datasets.CIFAR10(
    root = "./data",
    train = False,
    download = True,
    transform = transform
)

print("Number of training samples:", len(train_dataset))
print("Number of testing samples:", len(test_dataset))