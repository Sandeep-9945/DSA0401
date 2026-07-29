import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

# Load the dataset
data = pd.read_csv("C:/Users/sande/Downloads/data.csv")

# Stop words
stop_words = {
    "the", "and", "is", "a", "an", "of", "to",
    "in", "for", "on", "with", "this", "that",
    "it", "was", "are", "very"
}

# Combine all feedback
text = " ".join(data["feedback"].astype(str))

# Convert to lowercase and remove punctuation
text = text.lower()
words = re.findall(r'\b[a-z]+\b', text)

# Remove stop words
filtered_words = [
    word for word in words
    if word not in stop_words
]

# Calculate word frequency
frequency = Counter(filtered_words)

# Get user input for N
N = int(input("Enter the number of top words to display: "))

# Get top N words
top_words = frequency.most_common(N)

# Display results
print("\nTop", N, "Most Frequent Words:")

for word, count in top_words:
    print(word, ":", count)

# Prepare data for plotting
words = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

# Plot bar graph
plt.bar(words, counts)
plt.title("Top Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
