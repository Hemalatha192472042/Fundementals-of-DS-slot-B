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
