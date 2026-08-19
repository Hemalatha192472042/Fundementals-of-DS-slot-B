import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("../Datasets/patient_data.csv")

X = df[["Fever", "Cough", "Fatigue"]]
y = df["Condition"]

k = int(input("Enter value of K: "))

model = KNeighborsClassifier(n_neighbors=k)

model.fit(X, y)

fever = int(input("Fever (1/0): "))
cough = int(input("Cough (1/0): "))
fatigue = int(input("Fatigue (1/0): "))

patient = [[fever, cough, fatigue]]

prediction = model.predict(patient)

if prediction[0] == 1:
    print("Medical Condition: PRESENT")
else:
    print("Medical Condition: NOT PRESENT")
