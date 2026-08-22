-- Task 1: Introduction to Databases & SELECT Statement


-- 1. Display all records

SELECT *
FROM Students;


-- 2. Select specific columns

SELECT Name, Branch, Marks
FROM Students;


-- 3. Select student names and ages

SELECT Name, Age
FROM Students;


-- 4. Use column aliases

SELECT
    Name AS Student_Name,
    Branch AS Department,
    Marks AS Score
FROM Students;
