x = 2
w = 3

actual = 10

learning_rate = 0.1

for step in range(10):

    # 1. Forward pass
    prediction = x * w

    # 2. Calculate loss
    loss = 0.5 * (prediction - actual) ** 2

    # 3. Backpropagation
    gradient = prediction - actual
    gradient_w = gradient * x

    # 4. Update weight
    w = w - learning_rate * gradient_w

    print(
        f"Step {step + 1}: "
        f"Prediction = {prediction:.2f}, "
        f"Loss = {loss:.2f}, "
        f"Weight = {w:.2f}"
    )