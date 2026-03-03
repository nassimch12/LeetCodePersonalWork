-- Write your PostgreSQL query statement below
SELECT ranked_sal.depName AS "Department" , ranked_sal.empName AS "Employee", Salary AS "Salary"
FROM 
    ( SELECT Department.name AS depName, Employee.name AS empName, Salary, RANK() OVER (PARTITiON BY Department.id ORDER BY salary DESC) as rank
    FROM Department
    JOIN Employee ON department.id = Employee.departmentId
     ) AS ranked_sal

WHERE rank = 1

