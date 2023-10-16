-- The Most Active Students (kyu 5)
-- ####################################################################################################
-- https://www.codewars.com/kata/64a2a3d22bcea0046163eba8
-- In a prestigious UK university, students take different courses each term. A student's performance in a course is evaluated by a score.
-- As part of a yearly review, the university's administration wants to identify the most active students in the first term in the academic year 2022, which is called the "Michaelmas term". They're interested not just in the students' highest scores, but primarily in the total number of unique courses a student has taken during the term.
-- You have access to two tables: students and courses.
-- students:
-- | id  | name     | email               |
-- |-----|----------|---------------------|
-- | 1   | John     | john@example.com    |
-- | 2   | Sarah    | sarah@example.com   |
-- | 3   | Robert   | robert@example.com  |
-- ...
-- courses:
-- | id  | student_id | course_name | score |  course_date |
-- |-----|------------|-------------|-------|--------------|
-- | 1   | 1          | Math        | 90    | 2022-10-01   |
-- | 2   | 1          | Science     | 85    | 2022-10-15   |
-- | 3   | 1          | Physics     | 92    | 2023-01-10   |
-- | 4   | 1          | Literature  | 80    | 2023-04-05   |
-- ...
-- The students table has records of the students' id, name, and email. The courses table keeps a record of each course's id, the student_id of the student who took the course, the course name, the student's score in the course, and the date when the course was completed.
-- The output of the query should return the following columns:
-- student_id: The ID of the student.
-- name: The name of the student.
-- num_courses: The total count of unique courses that the student has taken during the term.
-- highest_scored_course: The course name and its score where the student achieved their highest score. It should be in the format "Course name (Score)". In the event of a tie (same score), choose the course with the latest date. If there's still a tie, choose the course that comes first alphabetically.
-- course_list: A string that consists of all the courses taken by the student with their respective dates and scores, separated by commas. The list of all courses should be in the format "Course name (Date - Score)", ordered by course date (from earlier to later) and then course name (in ascending order) in case of ties.
-- Order the result first by num_courses in descending order, then by the highest score in descending order, and, the the case of a tie even by the number of courses and the highest score - by student_id in ascending order.
-- Only the top 20 students based on the order criteria should be returned.
-- GLHF!
-- Notes:
-- Only consider courses completed between 1st October 2022 and 31st December 2022.
-- Desired Output
-- The desired output should look like this:
-- student_id        name        num_courses        highest_scored_course        course_list
-- 10        Zackary Nader        7        Course 7 (90)        Course 2 (2022-12-15 - 65), Course 4 (2022-12-15 - 75)...
-- 12        Gov. Reginald Boyle        7        Course 7 (90)        Course 1 (2022-12-15 - 60), Course 5 (2022-12-15 - 80), ...
-- 15        Fr. Ileana Will        7        Course 7 (90)        Course 1 (2022-12-15 - 60), Course 5 (2022-12-15 - 80)...

with relation as
(select c.*,s.name
from students s -- (2) students-courses position
left join   courses c
  on c.student_id = s.id 
where c.course_date >='2022-10-01' and c.course_date < '2022-12-31' -- (1) Only consider courses completed between 1st October 2022 and 31st December 2022.
)

,stud_max_score as (
select 
   student_id
  ,name
  ,score as highest_score
  ,course_name || ' ('||score||')' as highest_scored_course -- (3) whitespace and score between parentheses
from
(select student_id,name,course_name,score,row_number() 
                                            over(partition by student_id,name  -- (5) i use pair, cause might be one id - many full names or opposite case
                                                  order by 
                                                  score desc
                                                 ,course_date desc
                                                 ,course_name) rn
from relation
group by student_id,name,course_name,course_date,score -- (4) skip duplicates,also one student have one score
) q where rn=1
  
)

,num_course_sample as
(
select 
   r.student_id
  ,r.name
  ,count(distinct r.course_name) as num_courses
  ,string_agg(r.course_name || ' ('|| r.course_date || ' - '|| r.score ||')',', ' 
              order by r.course_date,r.course_name) as course_list -- (6) all courses with formating and order
from relation r
group by r.student_id,r.name
)


,res as 
(select 
   r.student_id
  ,r.name
  ,r.num_courses
  ,s.highest_scored_course
  ,r.course_list
from num_course_sample r
inner join stud_max_score s 
  on r.student_id = s.student_id and r.name = s.name -- (7) join by name and id to assemble parts togheter

order by r.num_courses desc,s.highest_score desc,r.student_id asc
 
limit 20 -- (8) slice sample with related order above
)

select *
from res