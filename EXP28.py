import pandas as pd
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("../Datasets/car_prices.csv")

X = df[["Mileage", "Age", "Engine"]]
y = df["Price"]

model = DecisionTreeRegressor(random_state=1)

model.fit(X, y)

mileage = float(input("Enter mileage: "))
age = float(input("Enter car age: "))
engine = float(input("Enter engine size: "))

prediction = model.predict([[mileage, age, engine]])

print("Predicted Car Price =", prediction[0])
