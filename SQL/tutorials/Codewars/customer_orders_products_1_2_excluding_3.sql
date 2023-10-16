-- Customer Orders: Products 1 & 2, Excluding 3 (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/64d9f2cd057026003eb4904f
-- Business sells only three unique products: "Product 1," "Product 2," and "Product 3."
-- Write an SQL query to find customers who have ordered "Product 1" and "Product 2" but not "Product 3." Additionally, provide a summary of how many times they have ordered the first two products.
-- Schema:
-- customers:
-- customer_id (integer) - primary key
-- name (varchar) - Name of the customer.
-- orders:
-- order_id (integer) - primary key
-- customer_id (integer) - Identifier for the customer who placed the order.
-- product_name (varchar) - Name of the ordered product. It can only be one of the three values: "Product 1," "Product 2," or "Product 3."
-- Write a query that returns the following columns:
-- customer_id: The unique identifier of the customer.
-- name: The name of the customer.
-- product_summary: A string that describes how many times the customer has ordered "Product 1" and "Product 2," formatted as "Product 1: {N} times || Product 2: {N} times."
-- The results should be ordered by customer_id in descending order.
-- GLHF!
-- Desired Output
-- The desired output should look like this:
-- customer_id	name	product_summary
-- 92	Jeri Auer	Product 1: 25 times || Product 2: 25 times
-- 83	Chang Sporer	Product 1: 8 times || Product 2: 8 times
-- 82	Regan Schimmel	Product 1: 15 times || Product 2: 15 times

with gb as 
(select 
   customer_id
  ,product_name
  ,count(*) cnt

from orders
group by 1,2
)

,agg as 
(select 
   gb.customer_id
  ,c.name 
  ,string_agg(product_name || ': ' || cnt || ' times' ,' || ' order by product_name asc ) as product_summary
from gb 
left join customers c using(customer_id )
group by 1,2 order by 1 desc
)

,filtered_products as 
(

select *
from agg 
where product_summary like '%Product 3%'

)

select *
from agg
where customer_id not in (select customer_id from filtered_products)
and product_summary like '%Product 1%' and product_summary like '%Product 2%'