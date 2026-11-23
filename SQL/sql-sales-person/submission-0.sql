-- Write your query below
SELECT name from sales_person
WHERE sales_id not in (SELECT sales_id from orders
JOIN company on orders.com_id = company.com_id
WHERE company.name = 'CRIMSON')