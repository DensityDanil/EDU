-- Backend Team's Tradition: An Age-Alternating Introduction (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/64b58b2b59329500245ffc22
-- When a new member joins the backend team, we have a tradition. Instead of the usual monotonous introductions, we introduce ourselves in an alternating age order - the youngest goes first, followed by the oldest, then the second youngest, the second oldest, and so on. This rollercoaster of introductions creates a fun and friendly atmosphere, breaking the ice for the newcomer and making them feel at home from day one.
-- We have employees with the the following columns:
-- employee_id: A unique integer identifier for each employee.
-- full_name: A string representing the employee's full name.
-- team: A string that specifies which team the employee is part of. The team can be one of the following four: "backend", "frontend", "devops", or "design".
-- birth_date: A date that represents the employee's birthdate.
-- Your task is to write a SQL query that will retrieve all employees from the 'backend' team, sorted according to this tradition. That is, they should be ordered by age in a unique alternating pattern: youngest first, then oldest, then second youngest, then second oldest, and so forth.
-- Your query should return a result set with columns: employee_id, full_name, team, birth_date, ordered as per the described pattern.
-- Notes:
-- Let's assume for this task that there are no developers with the same birth_date - tests are written to ensure that no two employees have the same birth date.
-- GLHF!
-- Desired Output
-- The desired output should look like this:
-- employee_id        full_name        team        birth_date
-- 4        Claris Kertzmann        backend        2004-04-11
-- 5        Venetta West V        backend        1971-05-17
-- 3        Tiara Breitenberg        backend        2002-02-16
-- 6        Ryan Harber        backend        1971-10-17

with tmp as 
(select 
  es.*
 ,row_number() over(order by birth_date desc) as youngest
 ,row_number() over(order by birth_date asc)+1 as oldest
from employees es
where team = 'backend'
order by birth_date desc)

,union_sample as 
(select 
   employee_id
  ,full_name
  ,birth_date
  ,team
  ,youngest
 
from tmp
union
select 
   employee_id
  ,full_name
  ,birth_date
  ,team
  ,oldest
from tmp
)

,rude as 
(select 
   employee_id
  ,full_name
  ,birth_date
  ,team
  ,row_number() over(partition by employee_id order by youngest asc,birth_date asc  ) as rn
from union_sample
order by youngest asc,birth_date asc
)

select 
   employee_id
  ,full_name
  ,birth_date
  ,team
from rude where rn=1