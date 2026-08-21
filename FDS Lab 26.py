# Question 26:
# Analyze clinical trial data using hypothesis testing and calculate
# the p-value to determine whether the new treatment has a
# statistically significant effect compared to the placebo.
# Visualize the data and p-value using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Read CSV file
df = pd.read_csv(r"C:\Users\sande\Downloads\Group,Result.csv")

# Separate groups
control = df[df["Group"] == "Control"]["Result"]
treatment = df[df["Group"] == "Treatment"]["Result"]

# Independent t-test
t, p = ttest_ind(control, treatment)

print("t-statistic:", t)
print("p-value:", p)

if p < 0.05:
    print("Treatment has a statistically significant effect.")
else:
    print("Treatment does not have a statistically significant effect.")

# Visualization
means = [control.mean(), treatment.mean()]

plt.bar(["Control", "Treatment"], means)
plt.ylabel("Mean Result")
plt.title("Control vs Treatment")
plt.show()

# P-value visualization
plt.bar(["p-value", "Significance Level"], [p, 0.05])
plt.ylabel("Value")
plt.title("P-value vs 0.05")
plt.show()
