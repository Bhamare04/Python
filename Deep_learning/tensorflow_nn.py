import tensorflow as tf

# 1. Load MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Normalize pixel values
# Original pixel values: 0 to 255
# Convert them to: 0 to 1
X_train = X_train / 255.0
X_test = X_test / 255.0

# 3. Build the neural network
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# 4. Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# 5. Train the model
model.fit(
    X_train,
    y_train,
    epochs=5
)

# 6. Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)

print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# 7. Save the trained model
model.save("mnist_model.keras")