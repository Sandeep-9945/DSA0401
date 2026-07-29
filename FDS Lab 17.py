import pandas as pd

# Create a Pandas DataFrame
data = {
    "Customer_Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Age": [25, 30, 25, 35, 30, 25, 40]
}

df = pd.DataFrame(data)

# Calculate frequency distribution of ages
frequency = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(frequency)
