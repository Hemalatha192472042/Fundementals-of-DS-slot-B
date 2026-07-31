import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/property_data.csv")
avg_price = df.groupby("Location")["ListingPrice"].mean()

print("Average Listing Price by Location")
print(avg_price)
count = len(df[df["Bedrooms"] > 4])

print("\nProperties with More Than 4 Bedrooms =", count)
largest = df.loc[df["Area"].idxmax()]

print("\nProperty with Largest Area")
print(largest)

# Draw Bar Graph
avg_price.plot(kind="bar")

plt.title("Average Listing Price by Location")
plt.xlabel("Location")
plt.ylabel("Average Listing Price")

plt.show()
