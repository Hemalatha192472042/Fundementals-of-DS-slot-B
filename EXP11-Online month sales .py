#11. Scenario : You are a data scientist working for a company that sells products online. You have been tasked with creating a simple plot to show the sales 
#of a product over time.
#Question: 
#1. Write code to create a simple line plot in Python using Matplotlib to predict sales happened in a month? 
#2. Write code to create a scatter plot in Python using Matplotlib to predict sales happened in a month? 
#3. Develop a Python program to create a bar plot of the monthly sales data. 





import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/monthly_sales.csv")

print("Monthly Sales Data")
print(df)

# Line Plot
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Month"], df["Sales"])
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
