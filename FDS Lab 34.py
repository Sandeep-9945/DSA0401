# Question 34:
# Perform Linear Regression to predict car prices based on selected
# features and identify the most influential factors affecting price.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Engine_Size,Horsepower,Fuel_Efficie.csv")

# Features and target
X = df[["Engine_Size", "Horsepower", "Fuel_Efficiency"]]
y = df["Price"]

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

# Influential factors
print("\nFeature Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(feature, ":", coef)
