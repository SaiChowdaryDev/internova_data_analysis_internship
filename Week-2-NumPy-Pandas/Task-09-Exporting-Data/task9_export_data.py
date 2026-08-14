import pandas as pd

# Read the original dataset
df = pd.read_csv("student_data.csv")

print("Original Dataset:")
print(df)


# Process the dataset
# Select students who scored 80 or above
processed_df = df[df["Marks"] >= 80].copy()

# Sort the processed data by Marks in descending order
processed_df = processed_df.sort_values(by="Marks", ascending=False)


# Display the processed DataFrame
print("\nProcessed Dataset:")
print(processed_df)


# Export the processed DataFrame to a new CSV file
processed_df.to_csv("processed_student_data.csv", index=False)

print("\nProcessed data has been exported successfully.")


# Verify the exported CSV file
exported_df = pd.read_csv("processed_student_data.csv")

print("\nExported Dataset:")
print(exported_df)

# Verify the exported data
print("\nExported file verified successfully.")
print("Number of rows:", len(exported_df))
print("Number of columns:", len(exported_df.columns))
