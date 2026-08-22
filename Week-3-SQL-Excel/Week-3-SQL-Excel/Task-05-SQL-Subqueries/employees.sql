-- Task 5: Employees Table

CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(30),
    Salary INT
);

INSERT INTO Employees (Employee_ID, Name, Department, Salary)
VALUES
(201, 'Amit', 'IT', 60000),
(202, 'Priya', 'HR', 45000),
(203, 'Rahul', 'IT', 75000),
(204, 'Sneha', 'Finance', 55000),
(205, 'Arjun', 'IT', 80000),
(206, 'Anjali', 'HR', 50000),
(207, 'Kiran', 'Finance', 65000),
(208, 'Meena', 'IT', 70000);
