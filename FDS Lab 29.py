# Question 29:
# Write a Python program that loads the Iris dataset from a CSV file
# and uses a Decision Tree classifier to predict the species of a new flower.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Read CSV file
df = pd.read_csv("iris_flowers.csv")

# Features and target
X = df[["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]]
y = df["Species"]

# Train Decision Tree
model = DecisionTreeClassifier(random_state=1)
model.fit(X, y)

# User input
sl = float(input("Enter sepal length: "))
sw = float(input("Enter sepal width: "))
pl = float(input("Enter petal length: "))
pw = float(input("Enter petal width: "))

flower = pd.DataFrame(
    [[sl, sw, pl, pw]],
    columns=["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]
)

prediction = model.predict(flower)

print("Predicted Species:", prediction[0])
