import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("../Datasets/bp_reduction.csv", sep=None, engine="python")
print(df.columns)
# Separate Drug and Placebo groups
drug = df[df["Group"] == "Drug"]["Reduction"]
placebo = df[df["Group"] == "Placebo"]["Reduction"]

# Calculate 95% confidence interval for Drug group
drug_ci = stats.t.interval(
    0.95,
    len(drug) - 1,
    loc=drug.mean(),
    scale=stats.sem(drug)
)

# Calculate 95% confidence interval for Placebo group
placebo_ci = stats.t.interval(
    0.95,
    len(placebo) - 1,
    loc=placebo.mean(),
    scale=stats.sem(placebo)
)

# Display results
print("Drug Group")
print("Mean Reduction =", drug.mean())
print("95% Confidence Interval =", drug_ci)

print("\nPlacebo Group")
print("Mean Reduction =", placebo.mean())
print("95% Confidence Interval =", placebo_ci)

# Draw graph
plt.figure(figsize=(7, 5))

plt.boxplot(
    [drug, placebo],
    labels=["Drug", "Placebo"]
)

plt.title("Blood Pressure Reduction")
plt.xlabel("Group")
plt.ylabel("Reduction")

# Save graph
plt.savefig("../Graphs/Exp22_BP_Confidence.png")

plt.show()
