#https://platform.stratascratch.com/coding/10090-find-the-percentage-of-shipable-orders?code_type=3
with tmp as 
(select 
     t1.* 
    ,t2.address
    ,case when t2.address is not null then 1 else 0 end as have_address
from orders t1
left join customers t2
    on t1.cust_id = t2.id)
    
,shipable_orders as 
(select sum(have_address)/count(have_address)*100
from tmp)


,shipable_orders_by_customer as 
(select cust_id,sum(have_address),count(have_address)
from tmp
group by cust_id
)


select *
from shipable_orders
-- where t2.address is not null
-- select *
-- from customers