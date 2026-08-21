# Question 23:
# Based on the data collected from the A/B test, is there a statistically
# significant difference in the mean conversion rates between website
# design A and website design B?

import pandas as pd
from scipy.stats import ttest_ind

# Read CSV file
df = pd.read_csv("conversion_rates.csv")

# Separate groups
A = df[df["Design"] == "A"]["Conversion_Rate"]
B = df[df["Design"] == "B"]["Conversion_Rate"]

# Independent t-test
t, p = ttest_ind(A, B)

print("t-statistic:", t)
print("p-value:", p)

if p < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")
