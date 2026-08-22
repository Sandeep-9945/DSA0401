# Question 30:
# Write a Python program using KNN to predict whether a new patient
# has a medical condition or not based on symptom features.

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Fever,Cough,Fatigue,Headache,Condit.csv")

# Features and target
X = df[["Fever", "Cough", "Fatigue", "Headache"]]
y = df["Condition"]

# User input
fever = int(input("Fever (0/1): "))
cough = int(input("Cough (0/1): "))
fatigue = int(input("Fatigue (0/1): "))
headache = int(input("Headache (0/1): "))
k = int(input("Enter k value: "))

# Train KNN
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
patient = pd.DataFrame(
    [[fever, cough, fatigue, headache]],
    columns=["Fever", "Cough", "Fatigue", "Headache"]
)

prediction = model.predict(patient)[0]

if prediction == 1:
    print("Patient has the medical condition.")
else:
    print("Patient does not have the medical condition.")
