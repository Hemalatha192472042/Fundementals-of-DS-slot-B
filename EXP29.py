from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier(random_state=1)

model.fit(X, y)

sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

flower = [[sepal_length, sepal_width,
           petal_length, petal_width]]

prediction = model.predict(flower)

print("Predicted Flower =", iris.target_names[prediction[0]])
