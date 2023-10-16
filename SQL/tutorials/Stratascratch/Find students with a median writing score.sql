#https://platform.stratascratch.com/coding/9610-find-students-with-a-median-writing-score?code_type=3
with precalc as 
(select 
sat_writing
,id
,row_number() over(order by sat_writing asc ) as rn
from sat_scores
order by 1 asc)

,median as 
(select *
from precalc
where rn in (select ceiling(max(rn)/2) from precalc)

)

select id
from sat_scores where sat_writing in (select sat_writing from median)
;