#https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=3
select cust_id, sum(total_order_cost) as s_total_order_cost
from orders
where order_date regexp '2019-03' 
group by cust_id
order by s_total_order_cost desc