-- Rolling Window Analysis of Customer Visits (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/64bf9096d914b5000e0cc73b
-- You are given a PostgreSQL table named customers, which keeps track of customer visits. The schema for the customers table is as follows:
-- date (date): The date when the customer visited.
-- customer_id (integer): The unique ID for each customer.
-- name (text): The name of the customer.
-- Here is some sample data:
-- date      |customer_id| name
-- ----------+-----------+-------
-- 2023-08-01| 1         | Andrew
-- 2023-08-02| 2         | Pete
-- 2023-08-03| 2         | Andrew
-- 2023-08-04| 2         | Steve
-- 2023-08-05| 2         | Stef
-- 2023-08-06| 3         | Stef
-- 2023-08-07| 1         | Jason
-- 2023-08-08| 1         | Jason
-- Your task is to write an SQL query that, for each row in the table, calculates the count of distinct names within the past two days (including the current day) for the same customer_id. The result should be ordered by the date in ascending order, then by customer_id in descending order, and finally by name in ascending order.
-- The output of your query should be all columns from customers table and count of integer type where the count of distinct names is shown that share the same customer_id within the past two days (including the current day).
-- So thus the result of your query from the sample data abobe should look something like this:
-- date      |customer_id| name  |count
-- ----------+-----------+-------+------
-- 2023-08-01| 1         |Andrew | 1
-- 2023-08-02| 2         |Pete   | 1
-- 2023-08-03| 2         |Andrew | 2
-- 2023-08-04| 2         |Steve  | 3
-- 2023-08-05| 2         |Stef   | 3
-- 2023-08-06| 3         |Stef   | 1
-- 2023-08-07| 1         |Jason  | 1
-- 2023-08-08| 1         |Jason  | 1

with stat as 
(select 
customer_id,date,   (select count(distinct name) 
                     from customers 
                         where customer_id=c.customer_id 
                         and (
                              date>=c.date-interval '2 days' and 
                              date<=c.date
                             ) 
                        ) as count
from customers c
group by customer_id,date      
)

select c.date,c.customer_id,c.name,s.count
from customers c
left join stat s using(date,customer_id)
order by c.date asc,c.customer_id desc,c.name asc