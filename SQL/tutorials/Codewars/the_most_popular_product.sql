-- The Most Popular Product (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/649d368a27e215c473e220ba
-- Let's consider a situation where we have three tables:
-- users table:
-- Columns: id, name
-- Primary key: id
-- products table:
-- Columns: id, product_name
-- Primary key: id
-- orders table:
-- Columns: id, user_id, product_id
-- Primary key: id
-- Foreign keys: user_id references users(id), product_id references products(id)
-- In this kata, we need to find the most popular product (i.e., the product that has been ordered the most). In case of a tie in the number of orders, return all most ordered products ordered by product ID in descending order. Include in the result also the total number of orders for that product.
-- GLHF!
-- Desired Output
-- The desired output should look like this:
-- product_id        product_name        count_orders
-- 2        Product2        20
-- 1        Product1        20

with 
calc as 
(select product_id,count(distinct id) d
from orders
group by product_id
order by 2 desc,product_id desc
)

,highest_sales as 
(select max(d) max_order_amount from calc)

,top_ordered_products as 
(select *
from calc
where d in (select max_order_amount from highest_sales)
)

select p.id as product_id, p.product_name, top_products.d count_orders
from top_ordered_products top_products
left join products p on p.id = top_products.product_id