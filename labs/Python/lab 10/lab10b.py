import matplotlib.pyplot as plt

income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

plt.figure(figsize=(8, 6))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Monthly Income by Source')
plt.axis('equal')
plt.show()
