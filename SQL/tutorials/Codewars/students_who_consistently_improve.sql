-- https://www.codewars.com/kata/649db77b6f8b2b00474fce2b/solutions/sql?filter=me&sort=best_practice&invalids=false
-- Your task is to identify students who have shown consistent improvement in their course scores over the three trimesters. 
-- The university is particularly interested in these students to understand and potentially replicate their success.

with student_term as 
(select 
   student_id
  ,score
  ,case 
    when extract(MONTH FROM course_date)  in (10,11,12) then '1.Michaelmas'
    when extract(MONTH FROM course_date)  in (1,2,3) then '2.Lent'
    when extract(MONTH FROM course_date)  in (4,5,6) then '3.Summer'
  end as term
from 
  courses
where 
  course_date >='2022-10-01' 
  and course_date<'2023-07-01'
)

,student_average_point as 
(select 
   student_id
  ,term
  ,avg(score) as avg_score_by_term
 
from student_term
group by student_id,term
order by 1,2 )

,better_avg_then_in_prev as
(select 
   sap.*
   ,avg_score_by_term>lag(avg_score_by_term) 
   over(partition by student_id order by term asc) as better_then_prev
  ,lag(avg_score_by_term) 
   over(partition by student_id order by term asc)
 
from student_average_point sap)

select 
   batip.student_id
  ,s.name
  ,string_agg(REGEXP_REPLACE(batip.term,'^[1-3]\.','') || ' (' || ROUND(batip.avg_score_by_term,2)::varchar || ')',', ' order by batip.term asc) trimesters_avg_scores
  ,string_agg(batip.better_then_prev::varchar,',' order by batip.term asc)= 'true,true' as consistent_improvement
from better_avg_then_in_prev batip
left join students s on s.id = batip.student_id 
group by batip.student_id, s.name
order by student_id DESC