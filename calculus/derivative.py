import sympy as sp

# x = sp.Symbol('x')
# f = x**2
# derivative = sp.diff(f,x)
# print("The derivative of", f, "with respect to x is:", derivative)

x, y = sp.symbols('x y')
f = x**4 + y*3
derivative_x = sp.diff(f, x)
derivative_y = sp.diff(f, y)
print("The derivative of", f, "with respect to x is:", derivative_x)
print("The derivative of", f, "with respect to y is:", derivative_y)