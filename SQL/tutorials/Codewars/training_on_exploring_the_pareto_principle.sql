-- Training on Exploring the Pareto Principle (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/645130c5680d5d006581ffe8/train/sql
-- In the task, you need to calculate whether a Pareto principle is observed for a DVD rentals, which states that 20% of customers will be responsible for approximately 80% of the rentals. You need to write a query that would identify the top 20% of customers based on the number of rentals they had made, and then calculate the percentage of total rentals they accounted for. In the task you need to:
-- calculate the total number of rentals across all customers.
-- identify the top 20% of customers by rentals.
-- calculate the number of rentals by these top 20% of customers.
-- Finally, to calculate the percentage of rentals by the top 20% of customers compared to the total number of rentals.
-- In your query you need to return three pieces of information:
-- top_20%_rentals_count: The total number of rentals made by the top 20% of customers.
-- total_rentals_count: The total number of rentals made by all customers.
-- percentage_of_top_20%: The percentage of total rentals made by the top 20% of customers. Should be of numeric type, rounded to 2 decimal places
-- Notes:
-- for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
-- Static dump won't provide belieavable percentage, but random test has been written to correlate with Pareto principle
-- What is meant by top 20% of customers? If there are 1000 customers in total, we would first order them by the number of rentals they have made, and then take the top 200 customers in terms of number of rentals. These 200 customers would be considered the "top 20%" of customers.
-- What we want to achieve is to cut off exactly 20% of customers regardless of tie. If 20 % is not the whole number - for example, for 599 customers it would be 119.8 - then we need to take upper bound, 120, not 119
-- Good luck!
-- Schema
-- (not all columns - only part of the domain required to solve this kata)
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
-- Desired Output
-- The desired output should look like this:
-- top_20%_rentals_count   | total_rentals_count  |     percentage_of_top_20%
-- -----------------------+----------------------+--------------------------+
-- 7756                 | 10000                |   0.776e2                |

with cra_all as
(   
  select q.*, row_number() over(order by ra desc) crn
  from
   (select 
     customer_id
    ,count(rental_id) ra
    from rental
    group by customer_id
    order by 2 desc) q 
)

,cra_top20_rounded_num as (   
    select round(count(*)::float*0.20) t20,count(*)::float
    from cra_all
)

,cra_top20_users  as (
    select *
    from cra_all
    where crn <= ( select t20 from cra_top20_rounded_num)
)

, cra_all_total as  ( select sum(ra) ra_total from cra_all )

     select 
      sum(ra)::int as "top_20%_rentals_count"
    , (select ra_total::int from cra_all_total ) as "total_rentals_count"
    , round(100*sum(ra)/( select ra_total from cra_all_total )::numeric,2) as "percentage_of_top_20%"
    from cra_top20_users