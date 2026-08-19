#14. Scenario: You are a data scientist working for an educational institution, and you want to explore  the correlation between students' study time 
#and their exam scores. You have collected data from a  group of students, noting their study time in hours and their corresponding scores in an exam. 
#Question: Identify any potential correlation between study time and exam scores and explore various  plotting functions to visualize this relationship 
#effectively. 




import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("../Datasets/study_performance.csv")

print("Student Study Data")
print(df)
correlation = df["StudyHours"].corr(df["ExamScore"])

print("\nCorrelation =", round(correlation,2))
plt.figure(figsize=(8,5))
plt.scatter(df["StudyHours"], df["ExamScore"])

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.savefig("../Graphs/Exp14_ScatterPlot.png")

plt.show()
plt.figure(figsize=(8,5))
plt.plot(df["StudyHours"], df["ExamScore"], marker='o')

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.savefig("../Graphs/Exp14_LinePlot.png")

plt.show()
