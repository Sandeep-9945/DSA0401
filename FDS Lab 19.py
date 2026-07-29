import pandas as pd
from collections import Counter
import re

# Create a DataFrame containing customer reviews
data = {
    "Review": [
        "Good product and good quality",
        "Excellent product and good service",
        "Good quality product"
    ]
}

df = pd.DataFrame(data)

# Combine all reviews into one text
text = " ".join(df["Review"]).lower()

# Extract words
words = re.findall(r'\b\w+\b', text)

# Calculate frequency distribution
frequency = Counter(words)

print("Frequency Distribution of Words:")

for word, count in frequency.items():
    print(word, ":", count)
