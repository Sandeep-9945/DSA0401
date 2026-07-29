import pandas as pd

# Sample sales DataFrame
sales_data = pd.DataFrame({
    'Product_Name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse',
                     'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Headphones'],
    'Quantity_Sold': [2, 5, 3, 4, 2, 1, 6, 3, 4, 5]
})

# Find the top 5 products sold the most
top_5_products = sales_data.groupby('Product_Name')['Quantity_Sold'] \
                           .sum() \
                           .sort_values(ascending=False) \
                           .head(5)

print("Top 5 Products Sold in the Past Month:")
print(top_5_products)
