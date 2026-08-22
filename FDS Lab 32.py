# Question 32:
# Write a Python program using Linear Regression to predict the price
# of a new house based on area, bedrooms and location.

import pandas as pd
from sklearn.linear_model import LinearRegression

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Area,Bedrooms,Location,Price.csv")

# Convert location to numbers
df["Location"] = df["Location"].map({
    "Urban": 0,
    "Suburban": 1,
    "Rural": 2
})

# Features and target
X = df[["Area", "Bedrooms", "Location"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter area (sq.ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
location = int(input("Enter location code (Urban=0, Suburban=1, Rural=2): "))

# Prediction
house = pd.DataFrame(
    [[area, bedrooms, location]],
    columns=["Area", "Bedrooms", "Location"]
)

price = model.predict(house)[0]

print("Predicted House Price:", round(price, 2), "Lakhs")
