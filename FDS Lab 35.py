# Question 35:
# Calculate accuracy, precision, recall and F1-score for a
# machine learning model using selected features and target variable.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Age,Blood_Pressure,Cholesterol,Cond.csv")

# User input
features = input("Enter feature names separated by comma: ").split(",")
target = input("Enter target variable: ")

features = [f.strip() for f in features]

# Features and target
X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Train model
model = DecisionTreeClassifier(random_state=1)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation metrics
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average="weighted"))
print("Recall:", recall_score(y_test, y_pred, average="weighted"))
print("F1-Score:", f1_score(y_test, y_pred, average="weighted"))
