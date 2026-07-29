# Item prices and quantities
prices = [50, 100, 200]
quantities = [2, 1, 3]

# Discount and tax rates
discount_rate = 10    # 10%
tax_rate = 5          # 5%

# Calculate total amount
total = sum(price * quantity for price, quantity in zip(prices, quantities))

# Calculate discount
discount = total * discount_rate / 100

# Amount after discount
amount_after_discount = total - discount

# Calculate tax
tax = amount_after_discount * tax_rate / 100

# Final amount
final_amount = amount_after_discount + tax

# Display results
print("Total Amount:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Amount to Pay:", final_amount)
