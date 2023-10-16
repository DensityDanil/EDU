-- Panda's leaked report with daily stats: Sales by 30 Minutes (kyu 5)
-- ####################################################################################################
-- https://www.codewars.com/kata/64ad157a0c6952004b172c5f
-- While visiting his favorite store, Panda, on May 9, 2023, one redditor found something interesting along with his purchase receipt. The store clerk accidentally included a printout of their daily sales statistics. He was amazed to see how detailed the sales data is: it breaks down the number and total amount of sales for each half-hour interval within the day, and even includes the percentage of sales for each interval compared to the total sales for the day!
-- sequence of moves for level1
-- Let's try and replicate this detailed sales report using PostgreSQL!
-- Create an SQL report to calculate the number and total amount of sales for each half-hour interval within a given day. The report should include the percentage of sales for each interval compared to the total sales for the day.
-- Let's assume you have access to a PostgreSQL database with a sales table. The sales table has the following schema:
-- id (integer): A unique identifier for each record.
-- timestamp (timestamp): The date and time of the sale.
-- amount (decimal): The amount of the sale.
-- You need to write an SQL query that generates a report with the following columns for May 8, 2023 from 10:00 AM to 10:30 PM:
-- Time: The half-hour interval, formatted as 'HH12:MI AM'-'HH12:MI AM' (for example, '10:00 AM-10:30 AM').
-- Cnt: The number of sales within the interval.
-- Sales: The total amount of sales within the interval. The currency symbol should be a dollar sign ('$'). The formatting should be handled by PostgreSQL's money datatype.
-- %Sales: The percentage of sales within the interval compared to the total sales for the day. This should be calculated as (interval sales / total sales) * 100, and rounded to two decimal places.
-- Notes:
-- If a sale occurrs exactly at 10:30, it will be included in the "10:30AM-11:00AM" interval, not the "10:00AM-10:30AM" interval. This is a common way to handle such situations in time series analysis and ensures that every sale belongs to exactly one interval.
-- You should include all intervals from 10:00 AM to 10:30 PM, even if there are no sales within some intervals.
-- The sales data may include multiple sales with the same timestamp. Make sure your query correctly handles this situation.
-- Sales are only made during the operating hours of 10:00 AM - 10:30 PM. There are no sales during this day that are out of the boundaries.
-- GLHF!
-- Desired Output
-- The desired output should look like this:
-- Time        Cnt        Sales        %Sales
-- 10:00 AM-10:30 AM        9        $ 915.08        0.535e1
-- 10:30 AM-11:00 AM        10        $ 804.87        0.471e1
-- 11:00 AM-11:30 AM        10        $ 854.03        0.5e1

select 
   to_char(t,'HH12:MI AM')||'-'||to_char(t+interval '30 minutes','HH12:MI AM') as "Time"
  ,coalesce(count(id),0) "Cnt"
  ,coalesce(sum(amount),0)::money as "Sales"
  ,coalesce(round(100*sum(amount)/ (sum(sum(amount)) over()),2),0.0) as "%Sales" -- NOTE crazy partition sum(sum())
--  ,coalesce(round(100*sum(amount) / (sum(sum(amount)) over()),2), 0.0) as "%Sales"

from generate_series( '2023-05-08 10:00'::timestamp
                ,'2023-05-08 22:30:00'
                ,'30 minutes') as gs(t)
left join (select distinct s.* from sales s) sales 
  on timestamp>=t and timestamp<t+interval '30 minutes'
  
group by t
order by t asc