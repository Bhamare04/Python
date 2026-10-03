import tensorflow as tf

x = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

y = [
    0,
    0,
    0,
    1
]

#convert the data in appropriate format
x= tf.constant(x, dtype=tf.float32)
y= tf.constant(y, dtype=tf.float32)

#build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

#compile and optimize
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#train the model
model.fit(x,y,epochs=500)

#evaluate the model
model.evaluate(x,y)

predictions = model.predict(x)

print("Predictions:", predictions)

#save the model
model.save("xor_model.keras")
