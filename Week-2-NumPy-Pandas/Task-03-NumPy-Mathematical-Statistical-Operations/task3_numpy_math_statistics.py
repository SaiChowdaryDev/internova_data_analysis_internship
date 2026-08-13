import numpy as np

# Create numerical datasets
data1 = np.array([10, 20, 30, 40, 50])
data2 = np.array([2, 4, 5, 8, 10])

print("Dataset 1:")
print(data1)

print("\nDataset 2:")
print(data2)

# Mathematical Operations

# Addition
addition = data1 + data2
print("\nAddition:")
print(addition)

# Subtraction
subtraction = data1 - data2
print("\nSubtraction:")
print(subtraction)

# Multiplication
multiplication = data1 * data2
print("\nMultiplication:")
print(multiplication)

# Division
division = data1 / data2
print("\nDivision:")
print(division)

# Statistical Operations
# Mean
mean = np.mean(data1)
print("\nMean:", mean)

# Median
median = np.median(data1)
print("Median:", median)

# Minimum
minimum = np.min(data1)
print("Minimum:", minimum)

# Maximum
maximum = np.max(data1)
print("Maximum:", maximum)

# Standard Deviation
standard_deviation = np.std(data1)
print("Standard Deviation:", standard_deviation)

# Sum
total = np.sum(data1)
print("Sum:", total)
