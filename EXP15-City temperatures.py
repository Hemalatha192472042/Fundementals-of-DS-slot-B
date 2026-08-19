#15. Scenario: You work for a weather data analysis company, and your team is responsible for developing a program to calculate and analyze variability in 
#temperature data for different cities. 
#Question: Write a python program will take in a dataset containing daily temperature readings for each  city over a year and perform the following tasks: 
#1. Calculate the mean temperature for each city. 
#2. Calculate the standard deviation of temperature for each city. 
#3. Determine the city with the highest temperature range (difference between the highest and lowest  temperatures). 
#4. Find the city with the most consistent temperature (the lowest standard deviation). 





import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/city_temperature.csv")

print("Temperature Dataset")
print(df)

# Mean temperature
mean_temp = df.groupby("City")["Temperature"].mean()

# Standard deviation
std_temp = df.groupby("City")["Temperature"].std()

# Temperature range
temp_range = df.groupby("City")["Temperature"].max() - df.groupby("City")["Temperature"].min()

print("\nMean Temperature")
print(mean_temp)

print("\nStandard Deviation")
print(std_temp)

print("\nTemperature Range")
print(temp_range)

print("\nCity with Highest Temperature Range:")
print(temp_range.idxmax())

print("\nMost Consistent City (Lowest Standard Deviation):")
print(std_temp.idxmin())

# Bar Graph
plt.figure(figsize=(8,5))
mean_temp.plot(kind="bar")

plt.title("Average Temperature of Cities")
plt.xlabel("City")
plt.ylabel("Mean Temperature (°C)")
plt.xticks(rotation=0)

plt.savefig("../Graphs/Exp15_BarGraph.png")

plt.show()
