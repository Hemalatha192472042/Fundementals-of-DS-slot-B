import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/customer_ages.csv")

print("Customer Age Data")
print(df)

# Frequency Distribution
age_frequency = df["Age"].value_counts().sort_index()

print("\nFrequency Distribution of Ages")
print(age_frequency)

# Bar Graph
plt.figure(figsize=(8,5))
age_frequency.plot(kind="bar")

plt.title("Frequency Distribution of Customer Ages")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.savefig("../Graphs/Exp17_AgeFrequency.png")

plt.show()
