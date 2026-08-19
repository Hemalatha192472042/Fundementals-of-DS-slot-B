#3. Scenario: You are working on a project that involves analyzing a dataset containing information about houses in a neighborhood. 
#The dataset is stored in a CSV file, and you have imported it into a NumPy array named house_data. Each row of the array represents a house, and the 
#columns contain  various features such as the number of bedrooms, square footage, and sale price. 
#Question: Using NumPy arrays and operations, how would you find the average sale price of houses  with more than four bedrooms in the neighborhood? 




import numpy as np
import matplotlib.pyplot as plt

house_data = np.genfromtxt(
    "house_data.csv",
    delimiter=",",
    skip_header=1
)
filtered = house_data[house_data[:, 0] > 4]

average_price = np.mean(filtered[:, 2])

print("Average Sale Price =", round(average_price, 2))

plt.figure(figsize=(6, 4))
plt.bar(filtered[:, 0].astype(int), filtered[:, 2])

plt.title("Bedrooms vs Sale Price")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Sale Price")

plt.savefig("house_graph.png")
print("Graph saved as house_graph.png")
