import pandas as pd
from scipy import stats

# Read CSV file
df = pd.read_csv("blood_pressure.csv")

# Separate groups
drug = df[df["Group"] == "Drug"]["Reduction"]
placebo = df[df["Group"] == "Placebo"]["Reduction"]

def CI(data):
    mean = data.mean()
    se = stats.sem(data)
    return stats.t.interval(0.95, len(data)-1,
                            loc=mean, scale=se)

print("95% CI for New Drug:", CI(drug))
print("95% CI for Placebo:", CI(placebo))
