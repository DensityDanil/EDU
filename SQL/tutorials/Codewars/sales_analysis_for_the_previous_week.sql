-- Sales Analysis for the Previous Week (kyu 7)
-- ####################################################################################################
-- https://www.codewars.com/kata/64d36a38e0d3a51afcd6e1ff
-- Write an SQL query to retrieve the total number of sales and total amount for each category for the previous week. The term "previous week" refers to the time period that begins on the Monday immediately preceding the current week and ends on the following Sunday. This time period is considered to be the last complete week that has passed.
-- Database Schema:
-- categories:
-- category_id (integer, primary key) - Unique identifier for the category.
-- category_name (varchar) - Name of the category (e.g., Electronics, Clothing).
-- products:
-- product_id (integer, primary key) - Unique identifier for the product.
-- category_id (integer, foreign key) - References the category_id in the categories table.
-- product_name (varchar) - Name of the product.
-- sales:
-- sale_id (integer, primary key) - Unique identifier for the sale.
-- product_id (integer, foreign key) - References the product_id in the products table.
-- sale_date (date) - The date when the sale occurred.
-- amount (integer) - The amount of the sale in currency.
-- Resultant Dataset:
-- category_name (text) - Name of the category.
-- total_products_sold (integer) - Count of sales within the previous week for the given category.
-- total_sales_amount (integer) - Total amount of sales within the previous week for the given category.
-- The results should be ordered by the count of sales in descending order, then by the total amount in descending order, and finally by the category name in ascending order.
-- GLHF!
-- Desired Output
-- The desired output should look like this:
-- category_name        total_products_sold        total_sales_amount
-- Electronics        7        1529
-- Clothing        7        1078
-- Furniture        7        1056
-- Books        7        465
-- Groceries        7        465
-- Beauty Products        5        1045
-- Sports Equipment        5        952

with date_features
as
(select 
s.*
,extract(week from sale_date ) as dt_week
,extract(year from sale_date ) as dy_year
,extract(isodow from sale_date )
from sales s
order by 3 desc)


select 
c.category_name
,count(sale_id) total_products_sold
,sum(df.amount) total_sales_amount 
from date_features df

left join products p on p.product_id = df.product_id
left join categories c on c.category_id  = p.category_id 
where df.dt_week=(select max(dt_week)-1
        from date_features)
group by c.category_name
order by 2 desc,3 desc