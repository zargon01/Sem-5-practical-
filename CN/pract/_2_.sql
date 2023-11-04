-- JOINS
    SELECT Employees.first_name, Employees.last_name, Departments.department_name
    FROM Employees
    INNER JOIN/LEFT JOIN/RIGHT JOIN/FULL JOIN Departments ON Employees.department_id = Departments.department_id;

-- SUBQUERY
    SELECT first_name, last_name, salary
    FROM Employees
    WHERE salary > (SELECT AVG(salary) FROM Employees);

-- VIEW
    -- creating view
        CREATE VIEW view_name AS
        SELECT column1, column2, ...
        FROM table_name
        WHERE condition;
    -- drop 
        DROP VIEW view_name;