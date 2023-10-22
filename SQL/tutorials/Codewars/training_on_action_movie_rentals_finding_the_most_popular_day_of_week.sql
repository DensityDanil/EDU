-- In this task you need to analyze the popularity of action movies by day of the week. Your goal is to determine which day of the week is the most popular for renting movies from "Action" category. In the resultant query you need to return film_id, film_title, and most_popular_day_of_week where most_popular_day_of_week is one of the following 3-letter abbreviations: MON, TUE, WED, THU, FRI, SAT, SUN. Result should be sorted by film title alphabetically, and if film title is the same - then by film_id in asc order.

-- Notes:
-- for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
-- "most popular" = the most amount of rentals happened on that day of week for the film. If there is a tie, then simply return the day of week that appears first in alphabetical order.
-- lets assume that every film has non zero amount of rentals
-- as a hint, it can be done without using window functions
-- Schema
-- (not all columns - part of the domain required to solve this kata)

-- film table:
-- Column           | Type     | Modifiers
-- -----------------+----------+----------
-- film_id          | integer  | not null
-- title            | varchar  | not null
-- film_category table:
-- Column      | Type      | Modifiers
-- ------------+---------- +----------
-- film_id     | smallint  | not null
-- category_id | smallint  | not null
-- category table:
-- Column      | Type      | Modifiers
-- ------------+-----------+----------
-- category_id | smallint  | not null
-- name        | text      | not null
-- rental table:
-- Column       | Type      | Modifiers
-- -------------+-----------+----------
-- rental_id    | integer   | not null
-- inventory_id | integer   | not null
-- rental_date  | timestamp | not null
-- return_date  | timestamp | 
-- inventory table:
-- Column       | Type      | Modifiers
-- ------------ +-----------+----------
-- inventory_id | integer   | not null
-- film_id      | smallint  | not null
-- Desired Output
-- The desired output should look like this:

-- film_id | film_title             | most_popular_day_of_week |
-- --------+------------------------+--------------------------|
--    324  | Django Unchained       | MON                      | 
--    14   | 12 Years a Slave       | SAT                      |
-- ...


select 
    film_id
   ,title as film_title
   ,rd_weekday as most_popular_day_of_week
--   ,c
--  ,rn
from
(select 
 f.film_id
,f.title 
,upper(left(to_char(rental_date , 'Day'),3)) as rd_weekday
,count(r.rental_id) c
,dense_rank() 
 over(partition by f.title
       order by 
               count(r.rental_id) DESC
              ,upper(left(to_char(r.rental_date , 'Day'),3)) ASC
              
     ) rn
 
from rental r
left join inventory i ON (r.inventory_id = i.inventory_id)
left join film f ON (f.film_id = i.film_id)
left join film_category fc ON (fc.film_id = f.film_id)
left join category c ON (c.category_id  = fc.category_id )
 
WHERE c.name='Action'
 
GROUP BY rd_weekday,f.title,f.film_id 
order by f.title ASC,f.film_id ASC) q
where rn=1