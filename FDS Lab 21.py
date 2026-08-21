import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv(r"C:\Users\sande\Downloads\Lab 21.csv")

print(df.mean())
print(df.median())
print(df.std())

df.boxplot(column=["Age","Fat"])
plt.show()

plt.scatter(df["Age"], df["Fat"])
plt.show()

stats.probplot(df["Fat"], plot=plt)
plt.show()
