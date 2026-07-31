import numpy as np
import matplotlib.pyplot as plt
student_scores = np.genfromtxt(
    "../Datasets/student_scores.csv",
    delimiter=",",
    skip_header=1
)

average_scores = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

print("Average Score of Each Subject")

for i in range(len(subjects)):
    print(subjects[i], ":", round(average_scores[i], 2))

highest = np.argmax(average_scores)

print("\nHighest Average Subject:", subjects[highest])

plt.bar(subjects, average_scores)

plt.title("Average Score of Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()
