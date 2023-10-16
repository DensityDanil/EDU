-- https://platform.stratascratch.com/coding/9781-find-the-rate-of-processed-tickets-for-each-type?code_type=3
select 
     type
    ,sum(processed)/count(complaint_id) as rate
from facebook_complaints
group by type
;
