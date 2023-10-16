#https://platform.stratascratch.com/coding/9845-find-the-number-of-employees-working-in-the-admin-department?code_type=3
select 
count(distinct worker_id)
from worker
where month(joining_date)>=04 and department='Admin'
;