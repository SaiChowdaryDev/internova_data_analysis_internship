-- Students Table

CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Branch_ID INT,
    Marks INT
);

INSERT INTO Students VALUES
(101, 'Sai', 1, 85),
(102, 'Rahul', 2, 78),
(103, 'Priya', 1, 92),
(104, 'Arjun', 3, 88),
(105, 'Anjali', 1, 75);
