# Question 31:
# Build a KNN classification model to predict treatment outcome
# ("Good" or "Bad") and evaluate it using accuracy, precision,
# recall and F1-score.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Age,Gender,Blood_Pressure,Cholester.csv")

# Convert categorical values
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df["Outcome"] = df["Outcome"].map({"Bad": 0, "Good": 1})

# Features and target
X = df[["Age", "Gender", "Blood_Pressure", "Cholesterol"]]
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("Predicted Results:", y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1-Score:", f1_score(y_test, y_pred, zero_division=0))
