-- Task 2: WHERE, ORDER BY & Aggregate Functions


-- 1. WHERE clause
-- Display students who scored more than 80

SELECT *
FROM Students
WHERE Marks > 80;


-- 2. Comparison operator
-- Display students whose age is 20

SELECT *
FROM Students
WHERE Age = 20;


-- 3. Another comparison operator
-- Display students who scored 85 or more

SELECT *
FROM Students
WHERE Marks >= 85;


-- 4. ORDER BY ascending
-- Display students from lowest marks to highest marks

SELECT *
FROM Students
ORDER BY Marks ASC;


-- 5. ORDER BY descending
-- Display students from highest marks to lowest marks

SELECT *
FROM Students
ORDER BY Marks DESC;


-- 6. COUNT()
-- Count total number of students

SELECT COUNT(*) AS Total_Students
FROM Students;


-- 7. SUM()
-- Calculate total marks

SELECT SUM(Marks) AS Total_Marks
FROM Students;


-- 8. AVG()
-- Calculate average marks

SELECT AVG(Marks) AS Average_Marks
FROM Students;


-- 9. MIN()
-- Find the lowest marks

SELECT MIN(Marks) AS Minimum_Marks
FROM Students;


-- 10. MAX()
-- Find the highest marks

SELECT MAX(Marks) AS Maximum_Marks
FROM Students;
