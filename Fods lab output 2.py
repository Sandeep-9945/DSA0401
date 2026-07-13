import numpy as np

# 3x3 matrix (Rows = Products, Columns = Sales Prices)
sales_data = np.array([
    [1200, 1500, 1300],
    [1800, 1700, 1600],
    [1400, 1550, 1450]
])

# Calculate average price of all products
average_price = np.mean(sales_data)

# Display sales data
print("Sales Data:")
print(sales_data)

# Display average price
print("\nAverage Price of All Products:", average_price)
