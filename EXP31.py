import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("../Datasets/patient_treatment.csv")

X = df[["Age", "BP", "Cholesterol"]]
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predictions:")
print(y_pred)

print("\nAccuracy =", accuracy_score(y_test, y_pred))
print("Precision =", precision_score(y_test, y_pred, pos_label="Good"))
print("Recall =", recall_score(y_test, y_pred, pos_label="Good"))
print("F1 Score =", f1_score(y_test, y_pred, pos_label="Good"))
