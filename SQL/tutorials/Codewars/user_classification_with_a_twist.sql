-- User Classification With a Twist (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/64a579dcdddc250831dfa2b7
-- Imagine a system where users are classified into one of two classes - 'a' or 'b'. A single user may belong to one class, or they may belong to both. Also, a unique aspect of this system is that a user may have multiple records of belonging to the same class, or they may belong to both classes multiple times.
-- Your task is to write a query that accurately counts the number of users in each class, with a special rule: If a user belongs to both classes, they should only be counted under class 'b'.
-- users table has the following schema:
-- id (integer): A unique identifier for each record.
-- user_id (integer): An identifier for each user. Note that the same user ID may appear multiple times if a user belongs to multiple classes.
-- class (char): The class a user belongs to. It can only be either 'a' or 'b'.
-- Your resulting output will include the following columns:
-- class (char): The class identifier. In this assignment, it can only be 'a' or 'b'.
-- count (integer): The number of unique users belonging to each class, considering the special rule that a user belonging to both 'a' and 'b' should only be counted under class 'b'.

with user_class_d as
(select user_id,count(distinct class) d
from users
group by user_id)


,prepare_to_calc as 
(select 
case when user_id in (select user_id from user_class_d where d=2 group by user_id)
then 'b'
when user_id not in (select user_id from user_class_d where d=2 group by user_id) then class
end as class
,user_id
from users)

,calc as (
select class,count(distinct user_id) count 
from prepare_to_calc
group by 1
)

select * from calc