import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("../Datasets/rare_elements.csv")

# Get concentration values
data = df["Concentration"].values

# User input
sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (example: 0.95): "))
precision = float(input("Enter desired level of precision: "))

# Select sample
sample = data[:sample_size]

# Point estimation
mean = np.mean(sample)

# Standard error
standard_error = stats.sem(sample)

# Confidence interval
confidence_interval = stats.t.interval(
    confidence_level,
    len(sample) - 1,
    loc=mean,
    scale=standard_error
)

print("\nPoint Estimate (Mean) =", mean)

print(
    "Confidence Interval =",
    confidence_interval
)

# Check precision
margin_of_error = (confidence_interval[1] - confidence_interval[0]) / 2

print("Margin of Error =", margin_of_error)

if margin_of_error <= precision:
    print("The desired level of precision is achieved.")
else:
    print("The desired level of precision is not achieved.")

# Plot
plt.hist(sample, bins=8)

plt.title("Rare Element Concentration")
plt.xlabel("Concentration")
plt.ylabel("Frequency")

plt.savefig("../Graphs/Exp24_Rare_Element.png")

plt.show()
