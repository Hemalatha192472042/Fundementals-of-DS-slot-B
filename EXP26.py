import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load CSV file
df = pd.read_csv("../Datasets/treatment_data.csv")

# Separate the two groups
control = df[df["Group"] == "Control"]["Improvement"]
treatment = df[df["Group"] == "Treatment"]["Improvement"]

# Calculate means
control_mean = control.mean()
treatment_mean = treatment.mean()

print("Control Group Mean =", control_mean)
print("Treatment Group Mean =", treatment_mean)

# Perform independent t-test
t_stat, p_value = ttest_ind(treatment, control)

print("\nT-statistic =", t_stat)
print("P-value =", p_value)

# Hypothesis decision
if p_value < 0.05:
    print("Result: The treatment has a statistically significant effect.")
else:
    print("Result: The treatment does not have a statistically significant effect.")

# Create bar plot
plt.bar(
    ["Control", "Treatment"],
    [control_mean, treatment_mean]
)

plt.title("Treatment Effect Comparison")
plt.xlabel("Group")
plt.ylabel("Mean Improvement")

plt.savefig("../Graphs/Exp26_Treatment_Test.png")

plt.show()
