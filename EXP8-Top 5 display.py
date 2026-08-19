#8. Scenario: You are a data scientist working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. 
#The data is stored in a Pandas data frame. 
#Question: How would you find the top 5 products that have been sold the most in the past month? 





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
