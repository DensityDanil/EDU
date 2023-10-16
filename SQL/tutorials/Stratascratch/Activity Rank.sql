#https://platform.stratascratch.com/coding/10351-activity-rank?code_type=3

with tmp
as 
(
select 
     from_user
    ,count(to_user) as total_emails
    ,row_number() over(order by count(to_user) desc) as rk
    ,dense_rank() over(order by count(to_user) desc,from_user asc) as dr
    ,group_concat(distinct to_user ) as lst
from google_gmail_emails
group by 
    from_user)
    
select 
     from_user
    ,total_emails
    ,dr
    -- ,lst
    -- ,row_number() over(order by dr asc) as rk2
from tmp
order by dr asc