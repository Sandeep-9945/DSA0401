import pandas as pd

# Sample DataFrame
property_data = pd.DataFrame({
    'Property_ID': [101, 102, 103, 104, 105],
    'Location': ['Chennai', 'Bangalore', 'Chennai', 'Hyderabad', 'Bangalore'],
    'Bedrooms': [3, 5, 4, 6, 2],
    'Area_sqft': [1500, 2500, 1800, 3200, 1400],
    'Listing_Price': [7500000, 12000000, 8500000, 15000000, 6500000]
})

# 1. Average listing price in each location
avg_price = property_data.groupby('Location')['Listing_Price'].mean()
print("Average Listing Price by Location:")
print(avg_price)

# 2. Number of properties with more than four bedrooms
count_bedrooms = property_data[property_data['Bedrooms'] > 4].shape[0]
print("\nProperties with More Than 4 Bedrooms:", count_bedrooms)

# 3. Property with the largest area
largest_property = property_data.loc[property_data['Area_sqft'].idxmax()]
print("\nProperty with the Largest Area:")
print(largest_property)
