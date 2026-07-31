import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/weather_data.csv")

print("Weather Data")
print(df)

# Line Plot for Temperature
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Temperature"], marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("../Graphs/Exp12_LinePlot.png")
plt.show()

# Scatter Plot for Rainfall
plt.figure(figsize=(8,5))
plt.scatter(df["Month"], df["Rainfall"])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.savefig("../Graphs/Exp12_ScatterPlot.png")
plt.show()
