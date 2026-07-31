import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/product_sales.csv")
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print("Top 5 Most Sold Products")
print(top_products)

# Draw Bar Graph
top_products.plot(kind="bar")

plt.title("Top 5 Most Sold Products")
plt.xlabel("Products")
plt.ylabel("Total Quantity Sold")

plt.show()
