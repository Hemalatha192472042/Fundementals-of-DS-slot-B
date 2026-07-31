import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string

# Read CSV file
df = pd.read_csv("../Datasets/customer_feedback.csv")

# Combine all reviews
text = " ".join(df["Review"].astype(str)).lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Stop words
stop_words = {
    "the","is","and","a","an","to","of","in","for","on","at",
    "this","that","it","i","was","with","my","so","very"
}

filtered_words = [word for word in words if word not in stop_words]

# Count frequency
frequency = Counter(filtered_words)

# User input
n = int(input("Enter Top N Words: "))

top_words = frequency.most_common(n)

print("\nTop", n, "Frequent Words")
print(top_words)

# Plot
x = [word for word, count in top_words]
y = [count for word, count in top_words]

plt.figure(figsize=(8,5))
plt.bar(x, y)
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.savefig("../Graphs/Exp20_TopWords.png")

plt.show()
