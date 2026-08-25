import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Student data
data = {
    "Branch": ["CSE", "CSE", "ECE", "ECE", "EEE", "CSE",
               "EEE", "ECE", "CSE", "EEE"],
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 4, 6, 5],
    "Attendance": [70, 75, 78, 80, 85, 90, 92, 76, 88, 82],
    "Marks": [55, 60, 65, 70, 75, 80, 88, 68, 78, 72]
}

df = pd.DataFrame(data)

# 1. Count Plot
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="Branch")
plt.title("Number of Students by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Students")
plt.show()


# 2. Box Plot
plt.figure(figsize=(7, 4))
sns.boxplot(data=df, x="Branch", y="Marks")
plt.title("Marks Distribution by Branch")
plt.xlabel("Branch")
plt.ylabel("Marks")
plt.show()


# 3. Heatmap
plt.figure(figsize=(7, 5))

correlation = df[["Study_Hours", "Attendance", "Marks"]].corr()

sns.heatmap(correlation, annot=True)
plt.title("Correlation Between Student Variables")
plt.show()


# 4. Pair Plot
sns.pairplot(df[["Study_Hours", "Attendance", "Marks"]])
plt.show()
