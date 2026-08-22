-- Task 2: Students Table

CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Branch VARCHAR(20),
    Marks INT
);

INSERT INTO Students (Student_ID, Name, Age, Branch, Marks)
VALUES
(101, 'Sai', 19, 'CSE', 85),
(102, 'Rahul', 20, 'ECE', 78),
(103, 'Priya', 19, 'CSE', 92),
(104, 'Arjun', 21, 'IT', 88),
(105, 'Anjali', 20, 'CSE', 75),
(106, 'Kiran', 19, 'EEE', 81),
(107, 'Sneha', 20, 'CSE', 90),
(108, 'Ravi', 21, 'IT', 72),
(109, 'Meena', 19, 'ECE', 86),
(110, 'Vijay', 20, 'CSE', 95);
