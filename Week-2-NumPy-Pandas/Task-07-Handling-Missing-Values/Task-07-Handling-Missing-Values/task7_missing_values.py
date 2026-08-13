import pandas as pd

# Read the dataset
df = pd.read_csv("student_missing_data.csv")

# Display the dataset before handling missing values
print("Dataset Before Handling Missing Values:")
print(df)


# 1. Identify missing values
print("\nMissing Values in Each Column:")
print(df.isnull())


# 2. Count missing values in each column
print("\nCount of Missing Values:")
print(df.isnull().sum())


# 3. Remove rows containing missing values
df_dropped = df.dropna()

print("\nDataset After Removing Rows with Missing Values:")
print(df_dropped)


# 4. Fill missing values using appropriate methods
df_filled = df.copy()

# Fill missing Age with the mean age
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())

# Fill missing Marks with the mean marks
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())

# Fill missing Attendance with the mean attendance
df_filled["Attendance"] = df_filled["Attendance"].fillna(
    df_filled["Attendance"].mean()
)

print("\nDataset After Filling Missing Values:")
print(df_filled)


# Check if any missing values remain
print("\nMissing Values After Filling:")
print(df_filled.isnull().sum())


# Explanation
print("\nWhy Handling Missing Data is Important:")
print("Handling missing data is important because missing values can")
print("affect analysis results and may lead to inaccurate conclusions.")
print("Properly handling missing values improves data quality and")
print("helps produce more reliable results in Data Analytics.")
