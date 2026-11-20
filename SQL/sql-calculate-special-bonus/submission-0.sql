-- Write your query below
SELECT employee_id,
case
when employee_id % 2 = 1 AND name not LIKE 'M%' then salary
when not (employee_id % 2 = 1 AND name not LIKE 'M%') then 0
END AS bonus
FROM employees
ORDER BY employee_id