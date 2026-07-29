import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12000, 15000, 18000, 16000, 20000, 22000]

# 1. Line Plot
plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Data - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Plot
plt.figure(figsize=(6,4))
plt.bar(months, sales)
plt.title("Monthly Sales Data - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
