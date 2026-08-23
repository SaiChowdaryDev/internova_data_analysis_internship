import numpy as np

# Student marks
marks = np.array([55, 60, 65, 68, 70, 72, 75, 78, 80, 82, 85, 90, 95, 150])

# Calculate Q1 and Q3
Q1 = np.percentile(marks, 25)
Q3 = np.percentile(marks, 75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Find outliers
outliers = marks[(marks < lower_limit) | (marks > upper_limit)]

print("Student Marks:", marks)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Outliers:", outliers)

print("\nExplanation:")
print("The IQR method is used to identify values that are unusually far from the other values.")
print("Outliers can affect the mean, standard deviation and other analysis results.")
