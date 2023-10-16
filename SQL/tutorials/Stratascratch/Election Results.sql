with voter_weight as 
(select 
     voter
    ,1/count(candidate) as voter_weight_value
    ,group_concat( candidate)
from voting_results
where candidate is not null and trim(candidate)<>''
group by voter
order by 2 desc)

,canditate_voter_relation as 
(select 
     candidate
    ,round(sum(voter_weight_value),3) as splitted_votes_sum
    ,count( voter) as count_voter
    ,count(distinct voter) as count_distinct_voter
    ,group_concat(distinct voter)
from voting_results vr
left join voter_weight vw
    using(voter)
where candidate is not null and trim(candidate)<>''
group by 
    vr.candidate)


,voter_lookup as 
(select *
from voter_weight
-- where voter='Christine'
-- where voter in ('Arthur','Betty','Joyce','Kathy','Paul','Terry','Victor') -- 1.25 for Kathy
where voter in ('Alan','Andrew','Benjamin','Bobby','Charles','Christine','Evelyn','Helen','Kathy','Matthew','Nancy')
-- 5.283
-- kathy have missed candidate
-- voter	candidate	voter_weight_value
-- Christine	Christine 	0.5
-- Christine	Ryan 	0.5
)

,distinct_voter_sum as (
select sum(count_distinct_voter)
from canditate_voter_relation
)

,distinct_voters_list as 
(select count(distinct candidate)
from voting_results
-- group by voter
)

,res_attempt as (
select *
from canditate_voter_relation
where splitted_votes_sum in (select max(splitted_votes_sum) from canditate_voter_relation)
order by 2 desc)


select candidate
from res_attempt