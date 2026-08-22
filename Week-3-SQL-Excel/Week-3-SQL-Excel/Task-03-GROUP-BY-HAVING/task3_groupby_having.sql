-- Task 3: GROUP BY & HAVING


-- 1. Group students by Branch
-- Count the number of students in each branch

SELECT
    Branch,
    COUNT(*) AS Total_Students
FROM Students
GROUP BY Branch;


-- 2. Calculate average marks for each branch

SELECT
    Branch,
    AVG(Marks) AS Average_Marks
FROM Students
GROUP BY Branch;


-- 3. Calculate total marks for each branch

SELECT
    Branch,
    SUM(Marks) AS Total_Marks
FROM Students
GROUP BY Branch;


-- 4. Use HAVING
-- Display only branches whose average marks are greater than 80

SELECT
    Branch,
    AVG(Marks) AS Average_Marks
FROM Students
GROUP BY Branch
HAVING AVG(Marks) > 80;


-- 5. GROUP BY with multiple aggregate functions

SELECT
    Branch,
    COUNT(*) AS Total_Students,
    AVG(Marks) AS Average_Marks,
    MIN(Marks) AS Minimum_Marks,
    MAX(Marks) AS Maximum_Marks
FROM Students
GROUP BY Branch;
