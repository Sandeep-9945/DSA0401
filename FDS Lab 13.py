import pandas as pd

# Read stock data from CSV file
data = pd.read_csv(r"C:\Users\sande\Downloads\Ex 12 .csv")

# Select the closing price column
closing_prices = data["Close"]

# Calculate statistics
mean_price = closing_prices.mean()
variance = closing_prices.var()
standard_deviation = closing_prices.std()

# Display results
print("Mean Closing Price:", mean_price)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)

# Provide insight
if standard_deviation < 5:
    print("The stock price has low variability.")
elif standard_deviation < 15:
    print("The stock price has moderate variability.")
else:
    print("The stock price has high variability.")
