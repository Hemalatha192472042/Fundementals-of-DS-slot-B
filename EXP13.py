import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/stock_price.csv")

print("Stock Price Data")
print(df)

# Calculate statistics
mean_price = df["Close"].mean()
std_price = df["Close"].std()
max_price = df["Close"].max()
min_price = df["Close"].min()

print("\nMean Closing Price =", round(mean_price,2))
print("Standard Deviation =", round(std_price,2))
print("Highest Closing Price =", max_price)
print("Lowest Closing Price =", min_price)

# Line Graph
plt.figure(figsize=(8,5))
plt.plot(df["Day"], df["Close"], marker='o')

plt.title("Stock Closing Prices")
plt.xlabel("Trading Day")
plt.ylabel("Closing Price")

plt.grid(True)

plt.savefig("../Graphs/Exp13_StockPrice.png")

plt.show()
