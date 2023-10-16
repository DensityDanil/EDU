-- Time difference between consecutive transactions for a specific customer (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/644f780d5017ed1da1cf6b7f
-- Given a table rental in the DVD rental database, write a SQL query to calculate the time since the previous rental for each rental transaction made by customers with IDs 1 and 2. The result should include the rental ID, customer ID, rental date, and time since the previous rental in days, hours, and minutes.
-- Notes:
-- for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
-- The final result should be sorted by customer ID and rental date in ascending order.
-- you should not bother about the formatting of time_since_previous_rental - simple subtracting of the dates will provide the correct output
-- rental_date should be desplayed as a text in the ISO 8601 format (for example 2005-02-26 19:42:04)
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
-- rental_date  | timestamp | not null
-- Desired Output
-- The desired output should look like this:
-- rental_id    | customer_id  | rental_date          | time_since_previous_rental
-- -------------+--------------+----------------------+----------------------------------------------
-- 5851      | 1            | 2005-02-26 19:42:04  |  <null>
-- 8399      | 1            | 2005-03-19 04:20:14  |  20 days 08:38:10

with sample as 
(select 
   r.customer_id
  ,r.rental_date
  ,r.rental_id
  ,lag(r.rental_date) over(partition by r.customer_id order by r.customer_id,r.rental_date asc ) as shft
from rental r
left join customer c
  on c.customer_id = r.rental_id
where r.customer_id in (1,2)
group by 1,2,3
order by r.customer_id,r.rental_date

)

,calc as 
(select 
  rental_id
 ,customer_id
 ,cast(rental_date as varchar) as rental_date
 ,to_char(rental_date-shft,'FMDD')||' days '||to_char(rental_date-shft,'HH24:MI:ss') as time_since_previous_rental
from sample s
-- where rental_id=76
group by 1,2,3,4
order by customer_id,rental_date)


select 
 rental_id
 ,customer_id
 ,cast(rental_date as varchar) as rental_date
 ,case 
     when time_since_previous_rental like '0 days %' 
     then replace(time_since_previous_rental,'0 days ','')
     when time_since_previous_rental like '1 days %' 
     then replace(time_since_previous_rental,'1 days ','1 day ')
     else time_since_previous_rental end as time_since_previous_rental
from calc c

-- ,to_timestamp(shft-rental_date, "DD HH")
-- ,EXTRACT(DAY FROM shft-rental_date)
-- ,CAST(EXTRACT(DAY FROM shft-rental_date) AS VARCHAR)|| ' days ' ||CAST(EXTRACT(HOUR FROM shft-rental_date) AS VARCHAR)|| ':' ||CAST(EXTRACT(MINUTE FROM shft-rental_date) AS VARCHAR)|| ':' ||CAST(EXTRACT(SECOND FROM shft-rental_date) AS VARCHAR)