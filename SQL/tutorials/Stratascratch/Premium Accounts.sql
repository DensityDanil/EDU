-- https://platform.stratascratch.com/coding/2097-premium-acounts?code_type=3


with 
check_next_week_appearance as (
select 
     t.account_id
    ,t.entry_date
    ,t2.account_id as hello_interval_world
from premium_accounts_by_day t
inner join premium_accounts_by_day t2
    on t.final_price!=0 
    and t2.final_price!=0
    and t2.account_id=t.account_id 
    and t2.entry_date = t.entry_date + interval 7 day
group by
     t.account_id
    ,t.entry_date
    ,t2.account_id
)

,res as 
(
select 
     pabd.entry_date
     
    -- ,group_concat(distinct case when pabd.final_price!=0 then pabd.account_id end) g_total_unique_paid
    -- ,group_concat(distinct case when pabd.final_price!=0 and check_next_week_appearance.account_id is not null then pabd.account_id end) g_total_unique_paid_next_week
    
    ,count(distinct case when pabd.final_price!=0 then pabd.account_id end) total_unique_paid
    ,count(distinct case when pabd.final_price!=0 and check_next_week_appearance.account_id is not null then check_next_week_appearance.account_id end) total_unique_paid_next_week
from premium_accounts_by_day pabd
left join check_next_week_appearance  
    ON check_next_week_appearance.entry_date = pabd.entry_date 
    AND check_next_week_appearance.account_id=pabd.account_id
group by pabd.entry_date order by pabd.entry_date asc
limit 7
)


select *
from res
