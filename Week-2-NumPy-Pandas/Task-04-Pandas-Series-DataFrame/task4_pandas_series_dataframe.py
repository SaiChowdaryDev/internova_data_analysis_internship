import pandas as pd

# 1. Create a Pandas Series
marks = pd.Series([85, 78, 92, 88, 75])

print("Pandas Series:")
print(marks)


# 2. Create a DataFrame containing student information
student_data = {
    "Name": ["Sai", "Rahul", "Priya", "Arjun", "Anjali"],
    "Age": [19, 20, 19, 21, 20],
    "Branch": ["CSE", "ECE", "CSE", "IT", "CSE"],
    "Marks": [85, 78, 92, 88, 75]
}

df = pd.DataFrame(student_data)

# 3. Display the DataFrame
print("\nStudent DataFrame:")
print(df)


# 4. Display column names
print("\nColumn Names:")
print(df.columns)


# 5. Display the index
print("\nDataFrame Index:")
print(df.index)


# 6. Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

# 7. Display the updated DataFrame
print("\nUpdated Student DataFrame:")
print(df)
