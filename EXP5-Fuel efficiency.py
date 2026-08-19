#5. Scenario: You are a data analyst working for a car manufacturing company. As part of your analysis,  you have a dataset containing information 
#about the fuel efficiency of different car models. The dataset is stored in a NumPy array named fuel_efficiency, where each element represents the fuel 
#efficiency (in miles per gallon) of a specific car model. Your task is to calculate the average fuel efficiency and  determine the percentage improvement 
#in fuel efficiency between two car models. 






import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
fuel_data = np.genfromtxt(
    "../Datasets/fuel_efficiency.csv",
    delimiter=",",
    skip_header=1,
    usecols=1
)

cars = ["Car1","Car2","Car3","Car4","Car5",
        "Car6","Car7","Car8","Car9","Car10"]
average = np.mean(fuel_data)
improvement = ((fuel_data[-1] - fuel_data[0]) / fuel_data[0]) * 100

print("Average Fuel Efficiency =", round(average,2), "mpg")
print("Percentage Improvement = {:.2f}%".format(improvement))
plt.bar(cars, fuel_data)
plt.title("Fuel Efficiency of Car Models")
plt.xlabel("Car Models")
plt.ylabel("Fuel Efficiency (mpg)")

plt.xticks(rotation=45)

plt.show()
