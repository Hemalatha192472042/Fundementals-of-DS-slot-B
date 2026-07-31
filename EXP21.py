import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read CSV file
df = pd.read_csv("../Datasets/hospital_data.csv")

print("Hospital Dataset")
print(df)

# Statistics
print("\nAge Statistics")
print("Mean =", df["Age"].mean())
print("Median =", df["Age"].median())
print("Standard Deviation =", df["Age"].std())

print("\nFat Statistics")
print("Mean =", df["Fat"].mean())
print("Median =", df["Fat"].median())
print("Standard Deviation =", df["Fat"].std())

# Boxplots
plt.figure(figsize=(8,5))
plt.boxplot([df["Age"], df["Fat"]], labels=["Age","Fat"])
plt.title("Boxplot of Age and Fat")
plt.savefig("../Graphs/Exp21_Boxplot.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Age"], df["Fat"])
plt.title("Age vs Fat")
plt.xlabel("Age")
plt.ylabel("Fat (%)")
plt.grid(True)
plt.savefig("../Graphs/Exp21_Scatter.png")
plt.show()

# Q-Q Plot for Age
plt.figure(figsize=(6,6))
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.savefig("../Graphs/Exp21_QQ_Age.png")
plt.show()

# Q-Q Plot for Fat
plt.figure(figsize=(6,6))
stats.probplot(df["Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Fat")
plt.savefig("../Graphs/Exp21_QQ_Fat.png")
plt.show()
