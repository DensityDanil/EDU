-- https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3
-- Given a table of purchases by date, calculate the month-over-month percentage change in revenue. The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.
-- The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.


with rev as (
select 
date_format(created_at,'%Y-%m')  as date_format_created_at
,sum(value) as sum_value
from sf_transactions
group by 1
)

select 
     date_format_created_at
     -- ,sum_value
    -- ,lag(sum_value) over(order by date_format_created_at asc) as lead_sum_value
    ,round(100*(sum_value/lag(sum_value) over(order by date_format_created_at asc))-100,2) as next_month
from rev
;