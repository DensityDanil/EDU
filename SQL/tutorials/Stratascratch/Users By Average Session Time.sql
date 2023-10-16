#https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=3
-- user_id	avg_session_duration
-- 0	1883.5
-- 1	35

with user_date_page_load_tmp as 
(select 
 user_id
,date(timestamp) as date_timestamp
,max(timestamp) as page_load_max_timestamp
from facebook_web_log 
where 
action='page_load' 
group by user_id,date_timestamp)

,user_date_page_exit_tmp as 
(select 
 user_id
,date(timestamp) as date_timestamp
,max(timestamp) as page_exit_max_timestamp
from facebook_web_log 
where 
action='page_exit' 
group by user_id,date_timestamp)


,user_date_page_load_page_exit as (
select 
     p_load.user_id
    ,p_load.date_timestamp
    ,timestampdiff(second,page_load_max_timestamp,page_exit_max_timestamp) as session_duration
from 
    user_date_page_load_tmp p_load
left join 
    user_date_page_exit_tmp p_exit
    using(user_id,date_timestamp)
group by
     1
    ,2
)

select 
user_id,round(avg(session_duration),2) as avg_session_duration
from user_date_page_load_page_exit
where session_duration is not null
group by user_id
;

-- select *
-- from facebook_web_log
-- where user_id=1