-- https://platform.stratascratch.com/coding/2053-retention-rate?code_type=3
-- Find the monthly retention rate of users for each account separately for Dec 2020 and Jan 2021. Retention rate is the percentage of active users an account retains over a given period of time. In this case, assume the user is retained if he/she stays with the app in any future months. For example, if a user was active in Dec 2020 and has activity in any future month, consider them retained for Dec. You can assume all accounts are present in Dec 2020 and Jan 2021. Your output should have the account ID and the Jan 2021 retention rate divided by Dec 2020 retention rate.

with 
sample_with_period as 
(
select 
     sf_events.*
    ,cast(date_format(date,'%Y-%m-01') as date) date_period
from sf_events
)


,sample_with_period_prev_period as
(
select date_period,next_period
from
(select 
     date_period
    ,lead(date_period) over(order by date_period asc) next_period
from sample_with_period) q
where date_period<>next_period
group by date_period,next_period
)

,retention2020_sample as 
(select 
         s2.date_period
        ,s2.account_id
        ,s2.user_id
        ,dateranges.next_period
        ,account_user_in_next_period.user_id as retained_user
from sample_with_period s2
left join sample_with_period_prev_period dateranges 
    on s2.date_period=dateranges.date_period
left join sample_with_period account_user_in_next_period
    on account_user_in_next_period.account_id=s2.account_id
    and account_user_in_next_period.user_id=s2.user_id
    and account_user_in_next_period.date_period=dateranges.next_period
)

,retention_calc as 
(select date_period,account_id,ROUND(count(distinct retained_user)/count(distinct user_id),2) retention_rate
from retention2020_sample
group by date_period,account_id
)

select 
     r2020.account_id
    ,r2021.retention_rate/r2020.retention_rate jan_dec_ratio
from 
    (select * 
    from retention_calc
    where date_period like '2020-12%') r2020
left join 
    (select * 
    from retention_calc
    where date_period like '2021-01%') r2021 
using(account_id)