-- https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=3
-- Rank guests based on the number of messages they've exchanged with the hosts. Guests with the same number of messages as other guests should have the same rank. Do not skip rankings if the preceding rankings are identical.
-- Output the rank, guest id, and number of total messages they've sent. Order by the highest number of total messages first.
-- select  *
-- from airbnb_contacts
-- where id_guest in
-- ('bb490ede-8a70-4d61-a2e8-625855a393e2',
-- '86b39b70-965b-479d-a0b0-719b195acea2')

with airbnb_contacts_tmp as (
select  
     id_guest
    ,sum(n_messages) as n_messages_sum

from 
    airbnb_contacts
group by 
    id_guest)

select 
      id_guest
     ,n_messages_sum
     ,dense_rank() over(order by n_messages_sum desc) as rn
from 
    airbnb_contacts_tmp

-- order by rn desc