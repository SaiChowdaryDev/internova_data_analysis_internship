-- Task 4: SQL Joins


-- INNER JOIN

SELECT
    s.Student_ID,
    s.Name,
    d.Branch_Name,
    s.Marks
FROM Students s
INNER JOIN Departments d
ON s.Branch_ID = d.Branch_ID;


-- LEFT JOIN

SELECT
    s.Student_ID,
    s.Name,
    d.Branch_Name,
    s.Marks
FROM Students s
LEFT JOIN Departments d
ON s.Branch_ID = d.Branch_ID;


-- RIGHT JOIN

SELECT
    s.Student_ID,
    s.Name,
    d.Branch_Name,
    s.Marks
FROM Students s
RIGHT JOIN Departments d
ON s.Branch_ID = d.Branch_ID;
