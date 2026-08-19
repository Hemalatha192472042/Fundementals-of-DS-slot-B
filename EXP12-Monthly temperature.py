#12. Scenario: You are working on a data analysis project that involves analyzing the monthly temperature and rainfall data for a city. You have a 
#dataset containing the monthly temperature and rainfall values for each month of a year. Your task is to develop a Python program that generates line  
#plots and scatter plots to visualize the temperature and rainfall data. 
#Question: 
#1. Develop a Python program to create a line plot of the monthly temperature data. 
#2: Develop a Python program to create a scatter plot of the monthly rainfall data. 





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
