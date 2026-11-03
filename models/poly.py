import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#generate synthetic data
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X + np.random.randn(100,1) * 2

#transform features to polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

#fit ploynomial regression model
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)

#plot results
import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Polynomial Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Polynomial Regression')
plt.legend()
plt.show()

#metric evaluation
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
