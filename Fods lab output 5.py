import numpy as np

# Fuel efficiency (MPG) of different car models
fuel_efficiency = np.array([22, 26, 30, 35])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate percentage improvement from Model 1 to Model 4
percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

# Display results
print("Average Fuel Efficiency:", average_efficiency, "MPG")
print("Percentage Improvement:", percentage_improvement, "%")
