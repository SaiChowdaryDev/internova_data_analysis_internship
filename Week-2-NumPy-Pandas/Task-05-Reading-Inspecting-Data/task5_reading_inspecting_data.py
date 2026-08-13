import pandas as pd

# Read the CSV file
df = pd.read_csv("student_data.csv")

# Display the complete dataset
print("Complete Dataset:")
print(df)

# Display the first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Check the number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())
