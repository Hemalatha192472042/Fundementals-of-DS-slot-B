import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../Datasets/house_prices_lr.csv")

X = df[["Area", "Bedrooms"]]
y = df["Price"]

model = LinearRegression()

model.fit(X, y)

area = float(input("Enter house area: "))
bedrooms = int(input("Enter number of bedrooms: "))

prediction = model.predict([[area, bedrooms]])

print("Predicted House Price =", prediction[0])
