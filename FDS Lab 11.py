import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 150, 180, 160, 220, 250]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 150, 180, 160, 220, 250]

plt.scatter(months, sales)
plt.title("Monthly Sales Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 150, 180, 160, 220, 250]

plt.bar(months, sales)
plt.title("Monthly Sales Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
