-- SQL Basics: Simple JOIN and RANK (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/58094559c47d323ebd000035
-- For this challenge you need to create a simple SELECT statement that will return all columns from the people table, and join to the sales table so that you can return the COUNT of all sales and RANK each person by their sale_count.
-- people table schema
-- id
-- name
-- sales table schema
-- id
-- people_id
-- sale
-- price
-- You should return all people fields as well as the sale count as "sale_count" and the rank as "sale_rank".
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

with user_sales as 
(select p.id,p.name,count(distinct sale) sale_count
from people p
left join sales s
  on p.id = s.people_id
group by p.id,p.name)

select 
   us.*
  ,dense_rank() over(order by sale_count desc) sale_rank
from user_sales us