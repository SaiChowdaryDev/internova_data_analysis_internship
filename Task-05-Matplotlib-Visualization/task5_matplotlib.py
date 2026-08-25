import matplotlib.pyplot as plt

# Student data
students = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
marks = [55, 60, 65, 70, 75, 80, 88, 68, 78, 72]
study_hours = [2, 3, 4, 5, 6, 7, 8, 4, 6, 5]

# 1. Line Chart
plt.figure(figsize=(7, 4))
plt.plot(students, marks, marker="o")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


# 2. Bar Chart
plt.figure(figsize=(7, 4))
plt.bar(students, marks)
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


# 3. Pie Chart
plt.figure(figsize=(6, 6))

branches = ["CSE", "ECE", "EEE", "MECH"]
student_count = [40, 25, 20, 15]

plt.pie(student_count, labels=branches, autopct="%1.1f%%")
plt.title("Students by Branch")
plt.show()


# 4. Histogram
plt.figure(figsize=(7, 4))
plt.hist(marks, bins=5)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


# 5. Scatter Plot
plt.figure(figsize=(7, 4))
plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
