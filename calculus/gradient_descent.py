import numpy as np

def gradient_descent(f, grad_f, x0, learning_rate=0.01, max_iter=1000, tol=1e-6):
    """
    Perform gradient descent optimization to find the minimum of a function.

    Parameters:
    f : callable
        The function to minimize.
    grad_f : callable
        The gradient of the function.
    x0 : numpy.ndarray
        Initial guess for the minimum.
    learning_rate : float, optional
        Step size for each iteration (default is 0.01).
    max_iter : int, optional
        Maximum number of iterations (default is 1000).
    tol : float, optional
        Tolerance for convergence (default is 1e-6).

    Returns:
    x_min : numpy.ndarray
        The point that minimizes the function.
    f_min : float
        The minimum value of the function.
    """
    x = x0
    for i in range(max_iter):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        
        # Check for convergence
        if np.linalg.norm(x_new - x) < tol:
            break
        
        x = x_new

    return x, f(x)

x = np.array([0.0, 0.0])  # Initial guess
y = gradient_descent(lambda x: x[0]**2 + x[1]**2, lambda x: np.array([2*x[0], 2*x[1]]), x)
print("The minimum point is:", y[0])
print("The minimum value is:", y[1])
