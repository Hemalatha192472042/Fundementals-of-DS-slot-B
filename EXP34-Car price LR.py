import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("../Datasets/car_price_lr.csv")

X = df[["Engine", "Horsepower", "Mileage"]]
y = df["Price"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict(X)

print("R2 Score =", r2_score(y, prediction))

engine = float(input("Enter engine size: "))
horsepower = float(input("Enter horsepower: "))
mileage = float(input("Enter mileage: "))

new_car = [[engine, horsepower, mileage]]

price = model.predict(new_car)

print("Predicted Car Price =", price[0])

print("\nFeature Coefficients:")
print("Engine =", model.coef_[0])
print("Horsepower =", model.coef_[1])
print("Mileage =", model.coef_[2])
