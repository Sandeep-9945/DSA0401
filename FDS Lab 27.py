import pandas as pd
import matplotlib.pyplot as plt
# Read the dataset from CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Lab - 27.csv")
# Find top 5 players with highest goals
print("Top 5 Players by Goals:")
print(df.nlargest(5, "Goals")[["Name", "Goals"]])
# Find top 5 players with highest salaries
print("\nTop 5 Players by Salary:")
print(df.nlargest(5, "Weekly_Salary")[["Name", "Weekly_Salary"]])
# Calculate average age
avg_age = df["Age"].mean()
print("\nAverage Age:", round(avg_age, 2))
# Display players above average age
print("\nPlayers Above Average Age:")
print(df[df["Age"] > avg_age][["Name", "Age"]])
# Count players based on their positions
position_count = df["Position"].value_counts()
# Display position distribution using a bar chart
position_count.plot(kind="bar")
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()
