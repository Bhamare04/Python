import sympy as sp
x = sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 1))
print("The definite integral of", f, "from 0 to 1 is:", definite_integral)
indefinite_integral = sp.integrate(f, x)
print("The indefinite integral of", f, "is:", indefinite_integral)