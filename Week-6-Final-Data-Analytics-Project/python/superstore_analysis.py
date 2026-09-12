import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# 1. Load dataset
# -----------------------------

file_path = "../data/Sample-Superstore.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 2. Basic inspection
# -----------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# -----------------------------
# 3. Remove duplicate rows
# -----------------------------

df = df.drop_duplicates()

# -----------------------------
# 4. Handle missing values
# -----------------------------

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

# -----------------------------
# 5. Descriptive statistics
# -----------------------------

print("\nDescriptive Statistics:")
print(df.describe())

# -----------------------------
# 6. Sales and Profit analysis
# -----------------------------

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nTotal Quantity:")
print(df["Quantity"].sum())

print("\nAverage Discount:")
print(df["Discount"].mean())

# -----------------------------
# 7. Category analysis
# -----------------------------

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# -----------------------------
# 8. Region analysis
# -----------------------------

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

# -----------------------------
# 9. Sub-category analysis
# -----------------------------

print("\nSales by Sub-Category:")
print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Sub-Category:")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False))

# -----------------------------
# 10. Correlation analysis
# -----------------------------

print("\nCorrelation Matrix:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].corr())

# -----------------------------
# 11. Outlier detection
# -----------------------------

Q1 = df["Profit"].quantile(0.25)
Q3 = df["Profit"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Profit"] < lower_limit) |
    (df["Profit"] > upper_limit)
]

print("\nNumber of Profit Outliers:")
print(len(outliers))

# -----------------------------
# 12. Create visualization folder
# -----------------------------

os.makedirs("../visualizations", exist_ok=True)

sns.set_theme(style="whitegrid")

# -----------------------------
# Chart 1 - Sales by Category
# -----------------------------

plt.figure(figsize=(8, 5))

df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
).plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../visualizations/sales_by_category.png")
plt.close()

# -----------------------------
# Chart 2 - Sales by Region
# -----------------------------

plt.figure(figsize=(8, 5))

df.groupby("Region")["Sales"].sum().sort_values(
    ascending=False
).plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../visualizations/sales_by_region.png")
plt.close()

# -----------------------------
# Chart 3 - Profit by Category
# -----------------------------

plt.figure(figsize=(8, 5))

df.groupby("Category")["Profit"].sum().sort_values(
    ascending=False
).plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../visualizations/profit_by_category.png")
plt.close()

# -----------------------------
# Chart 4 - Sales vs Profit
# -----------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit"
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("../visualizations/sales_vs_profit.png")
plt.close()

# -----------------------------
# Chart 5 - Sales by Sub-Category
# -----------------------------

plt.figure(figsize=(10, 6))

df.groupby("Sub-Category")["Sales"].sum().sort_values(
    ascending=False
).plot(kind="bar")

plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../visualizations/sales_by_subcategory.png")
plt.close()

# -----------------------------
# 13. Save cleaned dataset
# -----------------------------

df.to_excel(
    "../data/cleaned_superstore.xlsx",
    index=False
)

print("\nAnalysis completed successfully!")
print("5 visualizations created.")
print("Cleaned dataset saved successfully.")
