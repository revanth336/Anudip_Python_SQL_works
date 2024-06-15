import numpy as np
import matplotlib.pyplot as plt

# Sales data for different product categories
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Creating subplots to compare sales performance

plt.figure(figsize=(12, 8))

# Electronics Sales
plt.subplot(2, 2, 1)
plt.plot(months, electronics_sales, marker='o')
plt.title('Electronics Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)

# Clothing Sales
plt.subplot(2, 2, 2)
plt.plot(months, clothing_sales, marker='o')
plt.title('Clothing Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)

# Home & Garden Sales
plt.subplot(2, 2, 3)
plt.plot(months, home_garden_sales, marker='o')
plt.title('Home & Garden Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)

# Sports & Outdoors Sales
plt.subplot(2, 2, 4)
plt.plot(months, sports_outdoors_sales, marker='o')
plt.title('Sports & Outdoors Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)

plt.tight_layout()
plt.show()
