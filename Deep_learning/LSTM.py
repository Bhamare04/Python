from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM,Dense

#parameters
vocab_size = 10000
max_len = 200

#load the dataset
(x_train,y_train),(x_test,y_test) = imdb.load_data(num_words=vocab_size)

#pad the sequences
x_train = pad_sequences(x_train, maxlen=max_len)
x_test = pad_sequences(x_test, maxlen=max_len)

print(f"Training data shape: {x_train.shape}, Training labels shape: {y_train.shape}")
print(f"Test data shape: {x_test.shape}, Test labels shape: {y_test.shape}")

#Build the model
model =Sequential([
    Embedding(
        input_dim = vocab_size,
        output_dim=128
    ),
    LSTM(128,activation='tanh',return_sequences=False),

    Dense(1,activation='sigmoid')


])

#compile the model
model.compile(
    optimizer='adam',
    loss = 'binary_crossentropy',
    metrics=['accuracy']
)

#display model
model.summary()

history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.2
)


# -----------------------------
# 8. Evaluate model
# -----------------------------
loss, accuracy = model.evaluate(
    x_test,
    y_test
)

print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")