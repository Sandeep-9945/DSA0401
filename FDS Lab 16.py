from collections import Counter
import re

# Read the text file
with open("C:/Users/sande/Downloads/word.txt", "r") as file:
    text = file.read().lower()

# Extract words from the text
words = re.findall(r'\b\w+\b', text)

# Calculate word frequency
frequency = Counter(words)

# Display the frequency distribution
print("Word Frequency Distribution:")

for word, count in frequency.items():
    print(word, ":", count)
