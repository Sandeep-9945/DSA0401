# Question 25:
# Use the pandas library to calculate confidence intervals to estimate
# the true population mean rating from customer_reviews.csv.

import pandas as pd
from scipy import stats

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Rating.csv")

# Get ratings
ratings = df["Rating"]

# Calculate mean and standard error
mean = ratings.mean()
se = stats.sem(ratings)

# Calculate 95% confidence interval
ci = stats.t.interval(
    0.95,
    len(ratings) - 1,
    loc=mean,
    scale=se
)

print("Mean Rating:", mean)
print("95% Confidence Interval:", ci)
