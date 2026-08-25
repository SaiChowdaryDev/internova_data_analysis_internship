import pandas as pd
import numpy as np

# Create a sample student dataset
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 107],
    "Name": ["Arun", "Rahul", "Priya", "Sneha", "Kiran", "Ravi", "Anjali", "Anjali"],
    "Branch": ["CSE", "ECE", "CSE", "EEE", "CSE", "ECE", "CSE", "CSE"],
    "Study_Hours": [3, 4, np.nan, 5, 6, 4, 7, 7],
    "Attendance": [75, 80, 85, np.nan, 90, 78, 95, 95],
    "Marks": [65, 70, 75, 72, np.nan, 68, 88, 88]
}

df = pd.DataFrame(data)

# Display the dataset before cleaning
print("----- DATASET BEFORE CLEANING -----")
print(df)

# Basic data inspection
print("\n----- DATASET INFORMATION -----")
print("Number of rows and columns:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())

# Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# Check duplicate records
print("\nNumber of duplicate rows:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values with the column mean
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Display the cleaned dataset
print("\n----- DATASET AFTER CLEANING -----")
print(df)

# Check again for missing values and duplicates
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:", df.duplicated().sum())
