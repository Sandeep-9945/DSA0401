import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score": [45, 50, 55, 60, 65, 72, 78, 82, 88, 95]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["Study_Hours"].corr(df["Exam_Score"])

print("Correlation Coefficient:", correlation)

# Scatter plot
plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.title("Study Time vs Exam Scores")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.show()
