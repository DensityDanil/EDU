-- https://www.codewars.com/kata/6475a060e81712003cc2eb44/train/sql
-- DESCRIPTION:
-- In this task, you are given the DVD Rental database. Your objective is to write a SQL query that accomplishes the following:

-- Select rentals for a specific customer with customer_id = 1
-- For each day that the selected customer rented a movie, identify groups of consecutive rental days. In other words, find sequences of days where each day is directly following the previous one (e.g., 14th, 15th, and 16th of February would form a group of three consecutive days).
-- For each rental day, determine the size of its group of consecutive days.
-- Ensure each date appears only once in your results. If the customer rented more than one movie on the same day, that day should still only be counted once.
-- The output of your query should be a list of all rental dates for the selected customer, along with the size of the consecutive day group that each date belongs to. For dates that are not part of a consecutive sequence, the group size should be 1.

-- The result should consist of the following columns:

-- name: This column represents the full name of the customer. It is a concatenation of the first_name and last_name
-- date_rental_occurred: This column represents the date without the time component when the customer rented a DVD. The dates are sorted in ascending order (from the earliest to the latest).
-- consecutive_days: This column represents the size of the group of consecutive rental days that each date belongs to. For each rental day, it counts the number of consecutive days, including the day itself, during which the customer rented DVDs. If a date is not part of a consecutive sequence (i.e., the customer didn't rent a DVD on the day before or after), the group size is 1.
-- Notes:
-- for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
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
-- Desired Output
-- The desired output should look like this:

--   name        | date_rental_occurred   | consecutive_days
-- --------------+-----------------------+------------------
--  John Smith   | 2005-05-25            | 1             
--  John Smith   | 2005-05-28            | 1  
--  John Smith   | 2005-06-15            | 2             
--  John Smith   | 2005-06-16            | 2   
--  John Smith   | 2005-06-21            | 1
--  ...

-- Replace with your SQL
with sample as 
(
select r.*,CONCAT(c.first_name,' ',c.last_name) as name
from rental r
left join customer c
  using(customer_id  )
where c.customer_id=1
order by r.rental_date asc
)

,date_series as 
(
select 
   q.rental_date
  ,q.name
  ,LAG(q.rental_date) OVER(ORDER BY q.rental_date ASC) rental_date_prev
from 
    (select 
     rental_date::date
    ,name
    from sample
    group by 1,2) q
)

select 
   name
  ,q.rental_date date_rental_occurred
  ,COUNT(1) OVER(PARTITION BY interrupt_id) consecutive_days
from
(select 
   ds.*
  ,COALESCE(SUM(CAST(rental_date-rental_date_prev!=1 AS INT)) OVER(ORDER BY rental_date ASC),0) interrupt_id
from date_series ds ) q

-- res:
-- name	date_rental_occurred	consecutive_days
-- Mary Smith	2005-05-25	1
-- Mary Smith	2005-05-28	1
-- Mary Smith	2005-06-15	2
-- Mary Smith	2005-06-16	2
-- Mary Smith	2005-06-18	1
-- Mary Smith	2005-06-21	1
-- Mary Smith	2005-07-08	2
-- Mary Smith	2005-07-09	2
-- Mary Smith	2005-07-11	1
-- Mary Smith	2005-07-27	3
-- Mary Smith	2005-07-28	3
-- Mary Smith	2005-07-29	3
-- Mary Smith	2005-07-31	3
-- Mary Smith	2005-08-01	3
-- Mary Smith	2005-08-02	3
-- Mary Smith	2005-08-17	3
-- Mary Smith	2005-08-18	3
-- Mary Smith	2005-08-19	3
-- Mary Smith	2005-08-21	2
-- Mary Smith	2005-08-22	2