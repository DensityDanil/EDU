-- Students to expel (kyu 5)
-- ####################################################################################################
-- https://www.codewars.com/kata/64956edc8673b3491ce5ad2c
-- Let's consider a case where we have a students table and a courses table. The tables have the following structure:
-- students:
-- | id  | name     | email               |
-- |-----|----------|---------------------|
-- | 1   | John     | john@example.com    |
-- | 2   | Sarah    | sarah@example.com   |
-- | 3   | Robert   | robert@example.com  |
-- ...
-- courses:
-- | id  | student_id | course_name | score |
-- |-----|------------|-------------|-------|
-- | 1   | 1          | Math        | 90    |
-- | 2   | 1          | Science     | 85    |
-- | 3   | 1          | Physics     | 92    |
-- | 4   | 1          | Literature  | 80    |
-- ...
-- The university is considering expelling students who either quit their studies or are consistently performing poorly in their courses. A student who quits is defined as a student with no records in the courses table. A student who is performing poorly is defined as a student with 3 or more courses with a grade less than 60.
-- Write a SQL query that retrieves a list of students who qualify for expulsion based on the criteria described above.
-- The query should return the following columns:
-- student_id: The ID of the student
-- name: The name of the student
-- reason: The reason for expelling the student. It should say either "quit studying" if the student has no records in the courses table, or "failed in [List of Courses]" where [List of Courses] is a comma-separated list of the courses that the student has failed. Each course in the list should be followed by the grade in parentheses. Failed courses should be sorted in ascending alphabetical order.
-- The result should be ordered by the student ID in ascending order.
-- Good Luck!
-- Desired Output
-- The desired output should look like this:
-- student_id	name	reason
-- 10	James	failed in Math(59), Physics(57), Science(58)
-- 11	David	failed in Literature(58), Math(55), Physics(57), Science(56)
-- 12	Lucy	quit studying
-- 13	Daniel	quit studying
-- 14	Grace	quit studying

with 
poor as 
(select 
  s.id as student_id
 ,s.name 
 ,'failed in '||string_agg( c.course_name|| '(' ||c.score::varchar|| ')', ', ' order by c.course_name asc ) as reason
 ,count(distinct c.course_name) d
from courses c
left join students s on s.id = c.student_id
where c.score<60
group by 
  s.id
 ,s.name
)


select * from
(select student_id,name,reason
from poor
where d>=3
union 
select id,name,'quit studying'
from students
where id not in (select student_id from courses) )q
order by 1 asc