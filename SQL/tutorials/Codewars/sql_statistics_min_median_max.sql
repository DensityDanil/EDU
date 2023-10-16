-- SQL Statistics: MIN, MEDIAN, MAX (kyu 5)
-- ####################################################################################################
-- https://www.codewars.com/kata/58167fa1f544130dcf000317
-- For this challenge you need to create a simple SELECT statement. Your task is to calculate the MIN, MEDIAN and MAX scores of the students from the results table.
-- Tables and relationship below:
-- Resultant table:
-- min
-- median
-- max

with med as 
(select 
   r.*
  ,row_number() over(order by score asc) rn
from result r
order by score)

,median_calc as
(
select  
case 
when mod( (select (max(med.rn::numeric)/2::numeric) from med )  ,2)=1
then (select score 
      from med
      where rn=(select (max(med.rn::numeric)/2::numeric) from med ) 
     )
else 
  (
   select (sum(score)::numeric/2::numeric)::float
   from
   (select score
   from med where rn>=(select floor(max(med.rn::numeric)/2::numeric) from med ) 
   limit 2) q
  )
end as value
)

select 
 min(score)
,(select value from median_calc) as median
,max(score)
from med