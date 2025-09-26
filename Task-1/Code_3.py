from sklearn.linear_model import LinearRegression
import numpy as np

X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for 6:", model.predict(6))
