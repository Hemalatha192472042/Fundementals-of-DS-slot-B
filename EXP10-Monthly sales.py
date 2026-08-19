#10. Scenario: You are working on a data visualization project and need to create basic plots using Matplotlib. You have a dataset containing the monthly sales 
#data for a company, including the month  and corresponding sales values. Your task is to develop a Python program that generates line plots and  bar plots to 
#visualize the sales data. 
#Question: 
#1. How would you develop a Python program to create a line plot of the monthly sales data? 
#2: How would you develop a Python program to create a bar plot of the monthly sales data? 







import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/monthly_sales.csv")

print("Monthly Sales Data")
print(df)

# Line Plot
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker='o')

plt.title("Monthly Sales Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])

plt.title("Monthly Sales Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()
