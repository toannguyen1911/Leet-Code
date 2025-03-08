# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee e1 on e.id = e1.managerID 
GROUP BY e.name
HAVING COUNT(e.name) >= 5
