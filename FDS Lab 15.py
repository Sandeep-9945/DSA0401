import pandas as pd

# Read temperature data from CSV file
data = pd.read_csv("C:/Users/sande/Downloads/City,Temperature.csv")

# Group data city-wise
city_data = data.groupby("City")["Temperature"]

# 1. Calculate mean temperature
mean_temperature = city_data.mean()

# 2. Calculate standard deviation
standard_deviation = city_data.std()

# 3. Calculate temperature range
temperature_range = city_data.max() - city_data.min()

# Display results
print("Mean Temperature:")
print(mean_temperature)

print("\nStandard Deviation:")
print(standard_deviation)

print("\nTemperature Range:")
print(temperature_range)

# 4. City with highest temperature range
highest_range_city = temperature_range.idxmax()

# 5. City with most consistent temperature
most_consistent_city = standard_deviation.idxmin()

print("\nCity with Highest Temperature Range:",
      highest_range_city)

print("City with Most Consistent Temperature:",
      most_consistent_city)
