import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Student dataset
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Arun", "Rahul", "Priya", "Sneha", "Kiran", "Ravi", "Anjali"],
    "Branch": ["CSE", "ECE", "CSE", "EEE", "CSE", "ECE", "CSE"],
    "Study_Hours": [3, 4, 4.83, 5, 6, 4, 7],
    "Attendance": [75, 80, 85, 83.0, 90, 78, 95],
    "Marks": [65, 70, 75, 72, 74.67, 68, 88]
}

df = pd.DataFrame(data)

# Correlation between numerical variables
correlation = df[["Study_Hours", "Attendance", "Marks"]].corr()

print("----- CORRELATION MATRIX -----")
print(correlation)

# Heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True)
plt.title("Correlation Between Student Variables")
plt.show()

# Average marks by branch
branch_marks = df.groupby("Branch")["Marks"].mean()

print("\n----- AVERAGE MARKS BY BRANCH -----")
print(branch_marks)

# Average attendance
average_attendance = df["Attendance"].mean()

print("\nAverage Attendance:", round(average_attendance, 2))

# Average study hours
average_study_hours = df["Study_Hours"].mean()

print("Average Study Hours:", round(average_study_hours, 2))

# Print observations
print("\n----- KEY INSIGHTS -----")

print("1. Study hours have a positive relationship with marks.")
print("2. Attendance also has a positive relationship with marks.")
print("3. The average marks are different across the branches.")
