-- Write your PostgreSQL query statement below
SELECT DISTINCT p.email AS Email
FROM Person p
JOIN Person d ON p.email = d.email
WHERE p.id <> d.id;
