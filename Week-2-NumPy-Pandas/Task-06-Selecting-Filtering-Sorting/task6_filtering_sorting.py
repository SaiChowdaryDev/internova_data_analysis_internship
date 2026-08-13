import pandas as pd

# Read the student dataset
df = pd.read_csv("student_data.csv")

print("Original Dataset:")
print(df)


# 1. Select specific columns
print("\nSelected Columns (Name and Marks):")
print(df[["Name", "Marks"]])


# 2. Select specific rows
print("\nSelected Rows (First 3 Students):")
print(df.iloc[0:3])


# 3. Filter records based on a condition
print("\nStudents with Marks greater than 85:")
print(df[df["Marks"] > 85])


# 4. Apply multiple filtering conditions
print("\nCSE Students with Marks greater than 80:")
filtered_data = df[(df["Branch"] == "CSE") & (df["Marks"] > 80)]
print(filtered_data)


# 5. Sort data in ascending order
print("\nStudents Sorted by Marks (Ascending):")
ascending_data = df.sort_values(by="Marks", ascending=True)
print(ascending_data)


# 6. Sort data in descending order
print("\nStudents Sorted by Marks (Descending):")
descending_data = df.sort_values(by="Marks", ascending=False)
print(descending_data)
