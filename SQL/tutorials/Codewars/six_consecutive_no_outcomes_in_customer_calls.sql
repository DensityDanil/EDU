-- https://www.codewars.com/kata/64d499812df37400210180e4/sql
-- DESCRIPTION:
-- We're analyzing data for a customer support center for a tech company. The "No" outcomes represent failed attempts by companies automated voice assistant to understand customer requests.

-- Now, if the voice assistant fails to understand the same customer six times in a row, a live support agent takes over the call.

-- Table Schema (calls):

-- call_id (integer) - The unique identifier for each call.
-- user_id (integer) - The unique identifier for the customer.
-- outcome (varchar) - The outcome of the voice assistant's attempt to understand the customer's request. Can be either 'Yes' (understood) or 'No' (not understood).
-- date_of_call (timestamp) - The date and time when the call occurred.
-- Your task is to write a PostgreSQL query to find instances where the voice assistant failed to understand the same customer six times in a row. The result should include the details of the sixth consecutive "No" call.

-- The result set should include user_id (integer) and date_of_call (text) columns and be sorted by user_id and date_of_call in ascending order.

-- GLHF!

-- Notes:

-- It is guaranteed that each call for user has unique timestamp and in ascending chronological order.

-- If a user has 12 consecutive "No" outcomes, the query should only return the 6th "No," not both the 6th and 12th.

-- If a user has two separate series of 6 consecutive "No" outcomes, each separated by a different outcome, both occurrences of the 6th "No" should be returned.

-- Desired Output
-- The desired output should look like this:

-- user_id	date_of_call
-- 1	2022-01-01 00:50:00
-- 1	2022-01-01 02:00:00
-- 2	2022-01-01 01:20:00



with sequence_data as (
select 
     call_id
    ,user_id
    ,date_of_call
    ,lag(call_id) OVER(partition by user_id order by date_of_call asc) call_prev
from
(select 
   ROW_NUMBER() OVER(partition by user_id order by date_of_call asc) call_id
  ,user_id
  ,date_of_call
  ,outcome
from calls c) q
  
where outcome='No'
)

,sequence_params as 
(select 
     q.*
    ,COUNT(*) OVER(partition by user_id,interrupt_id) user_sequence_length
    ,ROW_NUMBER() OVER(partition by user_id,interrupt_id order by call_id) user_sequence_inner_idx
from
(select 
     *
    ,COALESCE(SUM(CAST(call_id-call_prev!=1 AS INT)) 
              OVER(partition by user_id ORDER BY call_id)
              ,0) interrupt_id
from sequence_data) q
)

,res as 
(
select user_id,date_of_call::TEXT
from sequence_params
where user_sequence_inner_idx=6
)

select *
from res
order by user_id, date_of_call asc