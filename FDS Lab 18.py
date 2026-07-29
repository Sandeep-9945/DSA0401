import pandas as pd

# Create a DataFrame containing likes received by posts
data = {
    "Post_ID": [1, 2, 3, 4, 5, 6, 7],
    "Likes": [100, 250, 100, 500, 250, 100, 750]
}

df = pd.DataFrame(data)

# Calculate frequency distribution of likes
frequency = df["Likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(frequency)
