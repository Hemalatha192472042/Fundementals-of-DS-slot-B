import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("../Datasets/house_bivariate.csv")

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict(X)

r2 = r2_score(y, prediction)

print("R2 Score =", r2)

area = float(input("Enter house area: "))

price = model.predict([[area]])

print("Predicted Price =", price[0])

plt.scatter(df["Area"], df["Price"])
plt.plot(df["Area"], prediction)

plt.title("House Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")

plt.savefig("../Graphs/Exp33_House.png")
plt.show()
