import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/social_media_likes.csv")

print("Social Media Likes Data")
print(df)

# Frequency Distribution
likes_frequency = df["Likes"].value_counts().sort_index()

print("\nFrequency Distribution of Likes")
print(likes_frequency)

# Bar Graph
plt.figure(figsize=(8,5))
likes_frequency.plot(kind="bar")

plt.title("Frequency Distribution of Likes")
plt.xlabel("Number of Likes")
plt.ylabel("Frequency")
plt.xticks(rotation=0)

plt.savefig("../Graphs/Exp18_LikesFrequency.png")

plt.show()
