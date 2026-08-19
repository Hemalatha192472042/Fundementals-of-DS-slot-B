#1. Scenario: You are working on a project that involves analyzing student performance data for a class of 32 students. The data is stored in a NumPy 
#array named student_scores, where each row represents a student and each column represents a different subject. The subjects are arranged in the  
#following order: Math, Science, English, and History. Your task is to calculate the average score for each subject and identify the subject with the 
#highest average score. 
#Question: How would you use NumPy arrays to calculate the average score for each subject and determine the subject with the highest average score? 
#Assume 4x4 matrix that stores marks of each student in given order. 






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
