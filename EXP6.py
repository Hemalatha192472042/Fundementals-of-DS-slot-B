import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/grocery_data.csv")

# Discount and Tax
discount_rate = 10
tax_rate = 5

# Calculate Item Cost
df["Total"] = df["Price"] * df["Quantity"]

# Total Amount
total_cost = df["Total"].sum()

# Apply Discount
discount = total_cost * discount_rate / 100
amount_after_discount = total_cost - discount

# Apply Tax
tax = amount_after_discount * tax_rate / 100
final_bill = amount_after_discount + tax

print("Total Cost =", total_cost)
print("Discount =", discount)
print("Tax =", tax)
print("Final Bill =", final_bill)

# Graph
plt.bar(df["Item"], df["Total"])

plt.title("Item-wise Purchase Cost")
plt.xlabel("Items")
plt.ylabel("Total Cost")

plt.xticks(rotation=45)

plt.show()
