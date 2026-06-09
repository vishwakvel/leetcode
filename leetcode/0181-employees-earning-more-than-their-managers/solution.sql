-- Write your PostgreSQL query statement below
SELECT emp.name as Employee
FROM Employee emp
JOIN Employee mgr ON emp.managerId = mgr.id
WHERE emp.salary > mgr.salary
