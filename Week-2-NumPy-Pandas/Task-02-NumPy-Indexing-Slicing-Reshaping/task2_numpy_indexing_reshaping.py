import numpy as np


numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


print("Original Array:")
print(numbers)

print("\nIndexing:")
print("First element:", numbers[0])
print("Fifth element:", numbers[4])
print("Last element:", numbers[-1])


print("\nSlicing:")
print("Elements from index 2 to 6:", numbers[2:7])
print("First five elements:", numbers[:5])
print("Last three elements:", numbers[-3:])


two_dimensional = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-Dimensional Array:")
print(two_dimensional)


print("\nRows and Columns:")
print("First row:", two_dimensional[0])
print("Second row:", two_dimensional[1])
print("First column:", two_dimensional[:, 0])
print("Second column:", two_dimensional[:, 1])


print("Element at row 2, column 3:", two_dimensional[1, 2])


original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("\nOriginal Array for Reshaping:")
print(original_array)

reshaped_array = original_array.reshape(3, 4)

print("\nReshaped Array (3 x 4):")
print(reshaped_array)


reshaped_array_2 = original_array.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(reshaped_array_2)
