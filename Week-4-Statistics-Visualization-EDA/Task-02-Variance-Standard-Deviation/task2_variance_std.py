import numpy as np

# Student marks
marks = [72, 85, 78, 90, 85, 88, 76, 92, 85, 80]

# Calculate variance and standard deviation
variance = np.var(marks)
standard_deviation = np.std(marks)

# Display the results
print("Student Marks:", marks)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)

# Explanation
print("\nExplanation:")
print("Variance shows how much the marks are spread out from the average.")
print("Standard deviation shows the typical amount of variation in the marks.")
