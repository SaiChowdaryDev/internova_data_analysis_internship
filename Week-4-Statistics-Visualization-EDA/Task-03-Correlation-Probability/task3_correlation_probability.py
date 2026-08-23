import numpy as np

# Student data
study_hours = [2, 3, 4, 5, 6, 7, 8, 4, 6, 5]
marks = [55, 60, 65, 70, 75, 80, 88, 68, 78, 72]

# Calculate correlation
correlation = np.corrcoef(study_hours, marks)[0, 1]

print("Study Hours:", study_hours)
print("Marks:", marks)
print("Correlation:", round(correlation, 2))

# Interpret the correlation
if correlation > 0:
    print("The relationship between study hours and marks is positive.")
elif correlation < 0:
    print("The relationship between study hours and marks is negative.")
else:
    print("There is no linear relationship.")

# Probability example
# Suppose we select one student randomly.
# 5 out of 10 students scored 75 or more.
students_with_high_marks = 5
total_students = 10

probability = students_with_high_marks / total_students

print("\nProbability Example:")
print("Students scoring 75 or more:", students_with_high_marks)
print("Total students:", total_students)
print("Probability:", probability)
print("Probability Percentage:", probability * 100, "%")
