from collections import Counter
import matplotlib.pyplot as plt
import string

# Read text file
with open("../Datasets/sample_text.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Calculate frequency
frequency = Counter(words)

print("Word Frequency Distribution\n")
print(frequency)

# Top 10 words
top_words = frequency.most_common(10)

words = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

# Bar Graph
plt.figure(figsize=(8,5))
plt.bar(words, counts)

plt.title("Top 10 Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.savefig("../Graphs/Exp16_WordFrequency.png")

plt.show()
