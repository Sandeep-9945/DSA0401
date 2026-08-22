# Question 33:
# Perform bivariate analysis and build a Linear Regression model
# to predict house prices based on house size.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Area,Bedrooms,Location,Price.csv")

# Feature and target
X = df[["Area"]]
y = df["Price"]

# Bivariate analysis
plt.scatter(X, y)
plt.xlabel("House Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("Bivariate Analysis: Area vs Price")
plt.show()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Regression line
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("Linear Regression: Area vs Price")
plt.show()
