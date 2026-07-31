import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string

# Read CSV file
df = pd.read_csv("../Datasets/customer_reviews.csv")

print("Customer Reviews")
print(df)

# Combine all reviews
text = " ".join(df["Review"].astype(str)).lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Count frequencies
frequency = Counter(words)

print("\nTop 10 Frequent Words")
print(frequency.most_common(10))

# Prepare graph data
top_words = frequency.most_common(10)

x = [word for word, count in top_words]
y = [count for word, count in top_words]

# Bar Graph
plt.figure(figsize=(8,5))
plt.bar(x, y)

plt.title("Top 10 Frequent Words in Customer Reviews")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.savefig("../Graphs/Exp19_WordFrequency.png")

plt.show()
