import numpy as np
from statistics import mode

# Student marks
marks = [72, 85, 78, 90, 85, 88, 76, 92, 85, 80]

# Calculate mean, median and mode
mean_marks = np.mean(marks)
median_marks = np.median(marks)
mode_marks = mode(marks)

# Display the results
print("Student Marks:", marks)
print("Mean:", mean_marks)
print("Median:", median_marks)
print("Mode:", mode_marks)

# Brief explanation
print("\nExplanation:")
print("Mean shows the average marks of the students.")
print("Median shows the middle value when the marks are arranged in order.")
print("Mode shows the mark that occurs most frequently.")
