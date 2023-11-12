-- https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=3
-- Find the popularity percentage for each user on Meta/Facebook. 
-- The popularity percentage is defined 
-- as the total number of friends the user has 
-- divided by the total number of users on the platform, 
-- then converted into a percentage by multiplying by 100. 
-- Output each user along with their popularity percentage. 
-- Order records in ascending order by user id. 
-- The 'user1' and 'user2' column are pairs of friends.


with friends_pairs as
(select user1 user_id,user2 
from facebook_friends
union
select user2,user1
from facebook_friends)

,all_users as 
(select user1 user_id 
from facebook_friends
union
select user2
from facebook_friends)

,all_users_count as (select count(*) c from all_users)

select user_id,count(distinct user2)/(select c from all_users_count)*100 AS popularity 
from friends_pairs
group by user_id
order by user_id
