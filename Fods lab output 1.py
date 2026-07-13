import numpy as np

# 4x4 matrix (Rows = Students, Columns = Subjects)
student_scores = np.array([
    [85, 78, 90, 88],
    [76, 82, 85, 80],
    [92, 88, 91, 87],
    [80, 75, 84, 89]
])

subjects = ["Math", "Science", "English", "History"]

# Calculate average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Find subject with highest average
highest_index = np.argmax(average_scores)

# Display averages
print("Average Scores:")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])

# Display highest average subject
print("\nSubject with Highest Average Score:")
print(subjects[highest_index], ":", average_scores[highest_index])
