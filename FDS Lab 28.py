# Question 28:
# Write a Python program using CART to predict the price of a new car
# and display the decision path for the prediction.

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\cars_prices.csv")

# Convert categorical data
df["Brand"] = df["Brand"].astype("category").cat.codes
df["Engine"] = df["Engine"].astype("category").cat.codes

X = df[["Mileage", "Age", "Brand", "Engine"]]
y = df["Price"]

# Train CART model
model = DecisionTreeRegressor(max_depth=4, random_state=1)
model.fit(X, y)

# User input
mileage = float(input("Enter mileage: "))
age = float(input("Enter car age: "))
brand = int(input("Enter brand code: "))
engine = int(input("Enter engine code: "))

new_car = pd.DataFrame(
    [[mileage, age, brand, engine]],
    columns=["Mileage", "Age", "Brand", "Engine"]
)

# Prediction
price = model.predict(new_car)[0]
print("\nPredicted Price:", price)

# Decision path
node = model.decision_path(new_car).indices

print("\nDecision Path:")
for n in node:
    print("Node:", n)
