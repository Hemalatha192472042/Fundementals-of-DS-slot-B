import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Datasets/soccer_players.csv")

print("Top 5 Players by Goals")
print(df.sort_values("Goals", ascending=False).head(5))

print("\nTop 5 Players by Salary")
print(df.sort_values("Salary", ascending=False).head(5))

average_age = df["Age"].mean()

print("\nAverage Age =", average_age)

print("\nPlayers Above Average Age")
print(df[df["Age"] > average_age][["Name", "Age"]])

position_count = df["Position"].value_counts()

print("\nPlayers by Position")
print(position_count)

position_count.plot(kind="bar")

plt.title("Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")

plt.savefig("../Graphs/Exp27_Position.png")
plt.show()
