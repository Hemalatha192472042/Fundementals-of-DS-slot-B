#4. Scenario: You are working on a project that involves analyzing the sales performance of a company  over the past four quarters. The quarterly sales 
#data is stored in a NumPy array named sales_data,  where each element represents the sales amount for a specific quarter. Your task is to calculate the  t
#otal sales for the year and determine the percentage increase in sales from the first quarter to the fourth  quarter. 
#Question: Using NumPy arrays and arithmetic operations calculate the total sales for the year and determine the percentage increase in sales from the first 
#quarter to the fourth quarter? 



import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
sales_data = np.genfromtxt(
    "../Datasets/quarterly_sales.csv",
    delimiter=",",
    skip_header=1,
    usecols=1
)

quarters = ["Q1", "Q2", "Q3", "Q4"]
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Annual Sales =", total_sales)
print("Percentage Increase = {:.2f}%".format(percentage_increase))

plt.plot(quarters, sales_data, marker='o')

plt.title("Quarterly Sales Performance")
plt.xlabel("Quarters")
plt.ylabel("Sales")

plt.grid(True)

plt.show()
