import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load CSV file
df = pd.read_csv("../Datasets/customer_satisfy_reviews.csv")

# Get ratings
ratings = df["Rating"]

# Calculate mean rating
mean_rating = ratings.mean()

# Calculate 95% confidence interval
confidence_interval = stats.t.interval(
    0.95,
    len(ratings) - 1,
    loc=mean_rating,
    scale=stats.sem(ratings)
)

print("Average Rating =", mean_rating)

print("95% Confidence Interval =",
      confidence_interval)

# Customer satisfaction
if mean_rating >= 4:
    print("Customer Satisfaction Level = High")
elif mean_rating >= 3:
    print("Customer Satisfaction Level = Moderate")
else:
    print("Customer Satisfaction Level = Low")

# Plot rating distribution
plt.hist(ratings, bins=5)

plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")

plt.savefig("../Graphs/Exp25_Customer_Ratings.png")

plt.show()
