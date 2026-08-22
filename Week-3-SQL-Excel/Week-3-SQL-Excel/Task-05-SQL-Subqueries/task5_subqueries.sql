-- Task 5: SQL Subqueries


-- Problem 1:
-- Find employees earning more than the average salary

SELECT
    Employee_ID,
    Name,
    Department,
    Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);


-- Problem 2:
-- Find employees earning the highest salary

SELECT
    Employee_ID,
    Name,
    Department,
    Salary
FROM Employees
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employees
);


-- Problem 3:
-- Find employees working in the same department as Rahul

SELECT
    Employee_ID,
    Name,
    Department,
    Salary
FROM Employees
WHERE Department = (
    SELECT Department
    FROM Employees
    WHERE Name = 'Rahul'
);
