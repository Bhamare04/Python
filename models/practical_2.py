#implement Linear Regression with the given dataset salary_data.csv .find the equation of the best fit line for this data.predict salary for 9.2 years of experience using prediction model.
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# a sample dataset consist of only two columns YearsExperience and Salary with 30 rows of data.
np.random.seed(42)
years_experience = np.random.uniform(0, 20, 30)
salary = 50000 + 10000 * years_experience + np.random.normal(0, 5000, 30)

df = pd.DataFrame({
    'YearsExperience': years_experience,
    'Salary': salary
})

X = df[['YearsExperience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Predict salary for 9.2 years of experience
predicted_salary = model.predict([[9.2]])
print(f"Predicted Salary for 9.2 years of experience: {predicted_salary[0]}")

slope = model.coef_[0]
intercept = model.intercept_
print(f"Equation of the best fit line: Salary = {slope} * YearsExperience + {intercept}")