-- Finding the Friday Night DVD Rental Kings/Queens (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/644b9b3b2ba287004f5d00f1
-- Write a SQL query using the DVD rental database to find the top 50 customers who rented movies on Friday between 6 pm and midnight (i.e. 18:00 to 23:59). For each customer, the query should return their id, full name, the total number of rentals they made on a Friday evening, and a comma-separated list of the dates (including the time) of those rentals, sorted in descending order.
-- Notes:
-- for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
-- by "top customers" is meant that list should be sorted by the quantity of rentals from higher to lower and if number of rentals is the same - then by last name of a customer
-- Good luck!
-- Schema
-- (not all columns - part of the domain required to solve this kata)
-- customer table:
-- Column       | Type     | Modifiers
-- ------------ +----------+----------
-- customer_id  | integer  | not null
-- first_name   | varchar  | not null
-- last_name    | varchar  | not null
-- rental table:
-- Column       | Type      | Modifiers
-- -------------+-----------+----------
-- rental_id    | integer   | not null
-- customer_id  | integer   | not null
-- rental_date  | timestamp | not null
-- return_date  | timestamp |
-- Desired Output
-- The desired output should look like this:
-- customer_id  | customer_name | friday_rentals | rental_dates
-- -------------+---------------+----------------+----------------------------------------------
-- 32        | Marcia Dean   | 14             | 2005-08-19 21:12:37, 2005-07-08 19:13:50  ...
-- 14        | Hosea Jacobi  | 10             | 2005-08-19 21:31:31, 2005-07-29 19:18:57 ...
-- ...

with slice_by_weeknum_and_hour
as
(select 
  c.customer_id  
 ,concat(c.first_name, ' ',  c.last_name) as customer_name       
 ,count(distinct rental_id) friday_rentals
 ,string_agg(to_char(rental_date, 'YYYY-MM-DD HH24:MI:SS'),', ' order by rental_date  desc ) rental_dates
from rental r
left join customer c using(customer_id)
where extract(isodow from rental_date  )= 5
and extract(hour from rental_date  ) between 18 and 23
 
group by c.customer_id,customer_name 
order by friday_rentals desc,c.last_name asc 
limit 50
)

select *
from slice_by_weeknum_and_hour