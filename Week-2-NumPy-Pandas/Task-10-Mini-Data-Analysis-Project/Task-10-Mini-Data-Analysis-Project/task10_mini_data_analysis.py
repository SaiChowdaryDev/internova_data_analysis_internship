import pandas as pd
import numpy as np

# Task 10: Mini Data Analysis Project
# Student Performance Analysis

# 1. Load the dataset
df = pd.read_csv("student_project_dataset.csv")

print("Original Dataset:")
print(df)

# 2. Data inspection
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# 3. Identify missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Handle missing values
cleaned_df = df.copy()
cleaned_df["Marks"] = cleaned_df["Marks"].fillna(cleaned_df["Marks"].mean())
cleaned_df["Attendance"] = cleaned_df["Attendance"].fillna(
    cleaned_df["Attendance"].mean()
)

print("\nDataset After Handling Missing Values:")
print(cleaned_df)

# 5. Select specific columns
print("\nSelected Columns:")
print(cleaned_df[["Name", "Branch", "Marks"]])

# 6. Filter data
print("\nStudents with Marks >= 80:")
print(cleaned_df[cleaned_df["Marks"] >= 80])

# 7. Sort data
print("\nStudents Sorted by Marks (Descending):")
sorted_df = cleaned_df.sort_values(by="Marks", ascending=False)
print(sorted_df)

# 8. GroupBy analysis
print("\nAverage Marks by Branch:")
groupby_result = cleaned_df.groupby("Branch")["Marks"].mean()
print(groupby_result)

# 9. Pivot Table
print("\nPivot Table - Average Marks and Attendance by Branch:")
pivot_result = pd.pivot_table(
    cleaned_df,
    values=["Marks", "Attendance"],
    index="Branch",
    aggfunc="mean"
)
print(pivot_result)

# 10. Useful insights
highest_student = cleaned_df.loc[cleaned_df["Marks"].idxmax(), "Name"]
highest_marks = cleaned_df["Marks"].max()
average_marks = cleaned_df["Marks"].mean()
best_branch = groupby_result.idxmax()

print("\nKey Insights:")
print(f"Highest scoring student: {highest_student} ({highest_marks:.2f} marks)")
print(f"Overall average marks: {average_marks:.2f}")
print(f"Branch with the highest average marks: {best_branch}")

# 11. Export cleaned dataset
cleaned_df.to_csv("cleaned_student_project_dataset.csv", index=False)

print("\nCleaned dataset exported successfully.")
