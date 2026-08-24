import sympy as sp

x,y = sp.symbols('x y')
f = x**2 + y**2
partial_derivative_x = sp.diff(f, x)
partial_derivative_y = sp.diff(f, y)
print("The partial derivative of", f, "with respect to x is:", partial_derivative_x)
print("The partial derivative of", f, "with respect to y is:", partial_derivative_y)