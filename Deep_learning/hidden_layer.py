# Inputs
x1 = 2
x2 = 3

# -------------------------
# Neuron 1
# -------------------------
w11 = 0.5
w12 = 0.4
b1 = 1

z1 = w11 * x1 + w12 * x2 + b1
h1 = max(0, z1)


# -------------------------
# Neuron 2
# -------------------------
w21 = 0.2
w22 = 0.7
b2 = 0

z2 = w21 * x1 + w22 * x2 + b2
h2 = max(0, z2)


# Print results
print("Neuron 1:")
print("z1 =", z1)
print("h1 =", h1)

print("\nNeuron 2:")
print("z2 =", z2)
print("h2 =", h2)

w21 = 0.2
w22 = 0.7
b2 = 0

z2 = w21 * x1 + w22 * x2 + b2
h2 = max(0, z2)


# =========================
# OUTPUT LAYER
# =========================

w31 = 0.6
w32 = 0.3
b3 = 0.5

z3 = w31 * h1 + w32 * h2 + b3


# =========================
# RESULTS
# =========================

print("Hidden neuron 1:", h1)
print("Hidden neuron 2:", h2)
print("Final output:", z3)