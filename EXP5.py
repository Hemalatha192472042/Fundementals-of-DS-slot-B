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
