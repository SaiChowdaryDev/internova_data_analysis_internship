import pandas as pd

# Read the two CSV datasets
df1 = pd.read_csv("students1.csv")
df2 = pd.read_csv("students2.csv")

print("Dataset 1:")
print(df1)

print("\nDataset 2:")
print(df2)


# -------------------------------------------------
# 1. MERGE
# -------------------------------------------------

merged_df = pd.merge(df1, df2, on="Student_ID")

print("\nMerged DataFrame:")
print(merged_df)


# -------------------------------------------------
# 2. CONCATENATE
# -------------------------------------------------

# Create another dataset with additional students
additional_students = pd.DataFrame({
    "Student_ID": [106, 107],
    "Name": ["Kiran", "Sneha"],
    "Branch": ["EEE", "CSE"],
    "Marks": [81, 90]
})

concatenated_df = pd.concat(
    [df1, additional_students],
    ignore_index=True
)

print("\nConcatenated DataFrame:")
print(concatenated_df)


# -------------------------------------------------
# 3. GROUPBY
# -------------------------------------------------

grouped_data = merged_df.groupby("Branch")["Marks"].mean()

print("\nAverage Marks by Branch:")
print(grouped_data)


# -------------------------------------------------
# 4. AGGREGATE FUNCTIONS
# -------------------------------------------------

aggregate_data = merged_df.groupby("Branch")["Marks"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print("\nAggregate Statistics by Branch:")
print(aggregate_data)


# -------------------------------------------------
# 5. PIVOT TABLE
# -------------------------------------------------

pivot_table = pd.pivot_table(
    merged_df,
    values="Marks",
    index="Branch",
    aggfunc="mean"
)

print("\nPivot Table - Average Marks by Branch:")
print(pivot_table)


# -------------------------------------------------
# 6. PIVOT TABLE WITH MULTIPLE VALUES
# -------------------------------------------------

pivot_table_multiple = pd.pivot_table(
    merged_df,
    values=["Marks", "Attendance"],
    index="Branch",
    aggfunc="mean"
)

print("\nPivot Table - Average Marks and Attendance by Branch:")
print(pivot_table_multiple)
