import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load CSV file
df = pd.read_csv("../Datasets/ab_test.csv")

# Separate Design A and Design B
design_a = df[df["Design"] == "A"]["ConversionRate"]
design_b = df[df["Design"] == "B"]["ConversionRate"]

# Calculate mean conversion rate
mean_a = design_a.mean()
mean_b = design_b.mean()

print("Mean Conversion Rate - Design A =", mean_a)
print("Mean Conversion Rate - Design B =", mean_b)

# Perform independent t-test
t_stat, p_value = ttest_ind(design_a, design_b)

print("\nT-statistic =", t_stat)
print("P-value =", p_value)

# Decision
if p_value < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")

# Bar graph
plt.bar(["Design A", "Design B"], [mean_a, mean_b])

plt.title("Comparison of Conversion Rates")
plt.xlabel("Website Design")
plt.ylabel("Mean Conversion Rate")

plt.savefig("../Graphs/Exp23_AB_Test.png")

plt.show()
