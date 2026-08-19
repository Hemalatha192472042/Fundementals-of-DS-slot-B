#7. Scenario: You are working as a data analyst for an e-commerce company. You have been given a  dataset containing information about customer orders, stored 
#in a Pandas DataFrame named order_data. The DataFrame has columns for customer ID, order date, product name, and order quantity.  Your task is to analyze the 
#data and answer specific questions about the orders. 
#Question: Using Pandas DataFrame operations, how would you find the following information from  the order_data DataFrame: 
#1. The total number of orders made by each customer. 
#2. The average order quantity for each product. 
#3. The earliest and latest order dates in the dataset. 






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
