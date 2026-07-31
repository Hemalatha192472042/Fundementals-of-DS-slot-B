import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/order_data.csv")
customer_orders = df["CustomerID"].value_counts()

print("Total Orders by Each Customer")
print(customer_orders)
average_quantity = df.groupby("Product")["Quantity"].mean()

print("\nAverage Order Quantity for Each Product")
print(average_quantity)
df["OrderDate"] = pd.to_datetime(df["OrderDate"], format="%d-%m-%Y")
print("\nEarliest Order Date:", df["OrderDate"].min())
print("Latest Order Date:", df["OrderDate"].max())

# Draw Bar Graph
customer_orders.plot(kind="bar")

plt.title("Total Orders by Each Customer")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")

plt.show()
