#https://platform.stratascratch.com/coding/10304-risky-projects?code_type=3
with tmp as 
(
select 
      prj.budget
     ,prj.title
     ,prj.start_date
     ,prj.end_date
     ,TIMESTAMPDIFF(day,prj.start_date,prj.end_date) as delta
     ,sal.salary/365 as calc -- TIMESTAMPDIFF(month,prj.start_date,prj.end_date) as calc
     ,TIMESTAMPDIFF(day,prj.start_date,prj.end_date)*(sal.salary/365) as calc2
     ,sal.*
from linkedin_projects prj -- Project37
inner join linkedin_emp_projects emp
    on concat('Project',emp.project_id) = prj.title
inner join linkedin_employees sal
    on emp.emp_id = sal.id
-- where prj.title = 'Project37'
)

select 
     title
    ,budget
    ,ceiling(sum(calc2)) as res
from tmp
group by 
     title
    ,2
having ceiling(sum(calc2))/budget>1
order by 
    sum(calc2)/budget desc
    
