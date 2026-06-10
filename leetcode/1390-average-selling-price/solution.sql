-- Write your PostgreSQL query statement below
SELECT p.product_id,
    CASE
        WHEN SUM(u.units) IS NULL THEN 0 
        ELSE ROUND(SUM(u.units * p.price) * 1.0 / SUM(u.units), 2)
    END AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
