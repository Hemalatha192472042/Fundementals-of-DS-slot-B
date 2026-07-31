import numpy as np
import matplotlib.pyplot as plt
sales_data = np.genfromtxt(
    "sales_data.csv",
    delimiter=",",
    skip_header=1
)
average_price = np.mean(sales_data)
print("Average Price of All Products =", round(average_price, 2))
product_average = np.mean(sales_data, axis=0)
products = ["Product1", "Product2", "Product3"]
plt.figure(figsize=(6, 4))
plt.bar(products, product_average)
plt.title("Average Sales of Products")
plt.xlabel("Products")
plt.ylabel("Average Price")
plt.savefig("sales_graph.png")
print("Graph saved as sales_graph.png")
