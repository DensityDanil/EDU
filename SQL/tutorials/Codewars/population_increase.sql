-- Population Increase (kyu 6)
-- ####################################################################################################
-- https://www.codewars.com/kata/6448fccc02d9290024ee766f
-- You are given a denormalized database table called world_population with columns id, country, year, and population. The table contains population data for various countries over the years.
-- Your task is to write a SQL query that finds the top 5 countries with the highest population increase strictly between the years 2000 and 2020, inclusive. The result should show the country name and the population increase in millions, rounded to 2 decimal places. The query should group the results by country and sort them in descending order based on the population increase.
-- Notes:
-- population_increase should be obtained by dividing the result by 1,000,000 to convert the number to millions, rounding it to 2 decimal places and afterwards by adding an abbreviation for millions, "M", to the end of result.
-- for the sample test is used static actual data taken from the United Nations, for the final solution - random test.
-- for this task there is no data missing, so you don't need to take into account that data for a year for some countries may be lacking
-- to avoid ambiguety: by "increase" is simply meant "population at year y1 - population at year y2".
-- Schema:
-- world_population table:
-- Column      | Type          | Modifiers
-- ------------+---------------+-----------
-- id          | integer       | not null
-- country     | varchar(255)  | not null
-- population  | bigint        | not null
-- year        | smallint      | not null
-- Desired Output
-- The desired output should look like this:
-- country      | population_increase
-- -------------+-------------------+
-- China        | 436.55 M          |
-- India        | 195.85 M          |
-- ...

with tmp as 
(
select 
country
,year as yr
-- ,round((lead(population) over(partition by country)-population)/1000000,2) as population_increase
,lead(population) over(partition by country order by year asc) as population_sft
,population
from world_population
where year between 2000 and 2020
order by country,year
)


,res_row as 
(select 
    tmp.country
   -- ,sum(population_sft-population) as  a
 ,ROUND( ( (sum(population_sft)::numeric - sum(population) )/1000000),2) ::numeric::float population_increase_val
from tmp
where population_sft is not null
group by 1
order by 2 desc limit 5)


select
 country
,TRIM (TO_CHAR(population_increase_val, '9999.00')||' M') as population_increase
from res_row