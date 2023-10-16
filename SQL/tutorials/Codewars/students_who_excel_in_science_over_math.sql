-- Students who excel in Science over Math (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/649421e15e89dc1ca27e5fb3
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
-- | 3   | 2          | Math        | 92    |
-- | 4   | 2          | Science     | 80    |
-- ...
-- We need to find the students who have a higher score in Science than in Math.
-- Your SQL query should return the student_id, name (the name of the student), and his or her difference in scores between these courses (named as score_difference).
-- Order the result by the difference in scores in descending order, and if diffrence is the same, then by student_id in ascending order.
-- Good Luck!
-- Desired Output
-- The desired output should look like this:
-- student_id	name	score_difference
-- 3	Robert	25
-- 5	Emma	3
-- 6	Olivia	2
-- 10	James	2

with courses_transpose as 
(select 
   student_id
  ,max(case when course_name='Math' then score end) as math_score
  ,max(case when course_name='Science' then score end) as science_score
from courses
group by student_id 
)
-- having science_score>math_score
select 
   ct.student_id
  ,ss.name
  -- ,science_score
  -- ,math_score
  ,science_score-math_score as score_difference
from courses_transpose ct
left join students ss on ss.id = ct.student_id
where science_score>math_score order by score_difference desc,ct.student_id asc