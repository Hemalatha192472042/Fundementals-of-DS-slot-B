import numpy as np
import matplotlib.pyplot as plt
house_data = np.genfromtxt(
    "../Datasets/house_data.csv",
    delimiter=",",
    skip_header=1
)
filtered = house_data[house_data[:,0] > 4]

average_price = np.mean(filtered[:,2])

print("Average Sale Price =", round(average_price,2))
plt.bar(filtered[:,0].astype(int), filtered[:,2])

plt.title("Bedrooms vs Sale Price")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Sale Price")

plt.show()
