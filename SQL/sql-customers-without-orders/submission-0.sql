-- Write your query below
SELECT customers.name FROM
customers
WHERE customers.id not in (SELECT customer_id from orders)