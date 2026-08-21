# Question 24:
# Write a Python program that allows the user to input the sample size,
# confidence level, and desired level of precision for estimating the
# population mean of rare element concentration.

import pandas as pd
import numpy as np
from scipy import stats

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\rare_elements.csv")

# User input
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired precision: "))

# Random sample
sample = df.iloc[:, 0].sample(n=n, random_state=1)

# Point estimation
mean = np.mean(sample)
std = np.std(sample, ddof=1)
se = std / np.sqrt(n)

# Confidence interval
alpha = 1 - confidence / 100
t_value = stats.t.ppf(1 - alpha / 2, n - 1)

margin = t_value * se
lower = mean - margin
upper = mean + margin

print("\nPoint Estimate (Mean):", mean)
print("Confidence Interval:", (lower, upper))
print("Margin of Error:", margin)

if margin <= precision:
    print("Desired precision is achieved.")
else:
    print("Desired precision is not achieved.")
