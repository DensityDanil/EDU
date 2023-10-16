-- Using Window Functions To Get Top N per Group (kyu 5)
-- ####################################################################################################
-- https://www.codewars.com/kata/582001237a3a630ce8000a41
-- Given the schema presented below write a query, which uses a window function, that returns two most viewed posts for every category.
-- Order the result set by:
-- category name alphabetically
-- number of post views largest to lowest
-- post id lowest to largest
-- Note:
-- Some categories may have less than two or no posts at all.
-- Two or more posts within the category can be tied by (have the same) the number of views. Use post id as a tie breaker - a post with a lower id gets a higher rank.
-- Schema
-- categories
-- Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- id          | integer                     | not null
-- category    | character varying(255)      | not null
-- posts
-- Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- id          | integer                     | not null
-- category_id | integer                     | not null
-- title       | character varying(255)      | not null
-- views       | integer                     | not null
-- Desired Output
-- The desired output should look like this:
-- category_id | category | title                             | views | post_id
-- ------------+----------+-----------------------------------+-------+--------
-- 5           | art      | Most viewed post about Art        | 9234  | 234
-- 5           | art      | Second most viewed post about Art | 9234  | 712
-- 2           | business | NULL                              | NULL  | NULL
-- 7           | sport    | Most viewed post about Sport      | 10    | 126
-- ...
-- category_id - category id
-- category - category name
-- title - post title
-- views - the number of post views
-- post_id - post id

with rel_as_it_is as 
(select 
   c.id as category_id
  ,c.category
 
  ,p.title
  ,p.views
  ,p.id as post_id
  ,dense_rank() over(partition by c.id order by p.views desc, p.id asc) as dr -- NOTE important to set relative column alias for partition to table in FROM clause
  
from categories c 
left join posts p on c.id = p.category_id
)


,rel_reverse as (
select 
   p.category_id
  
  ,c.category
  
  ,p.title
  ,p.views
  ,p.id as post_id
  ,dense_rank() over(partition by p.category_id order by p.views desc, p.id asc) as dr -- NOTE important to set relative column alias for partition to table in FROM clause
  
from posts p 
left join categories c on c.id = p.category_id

)


,first_part as 
(select 
   category_id
  ,category
  ,title
  ,views
  ,post_id
from rel_as_it_is
where (dr<=2 OR dr is null)
 
union
 
select 
   category_id
  ,category
  ,title
  ,views
  ,post_id
from rel_reverse
where (dr<=2 OR dr is null)

)


select *
from first_part
order by category,views desc,post_id asc
