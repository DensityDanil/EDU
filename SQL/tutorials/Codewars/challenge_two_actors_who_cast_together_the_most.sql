-- Challenge: Two actors who cast together the most (kyu 4)
-- ####################################################################################################
-- https://www.codewars.com/kata/5818bde9559ff58bd90004a2
-- Given the the schema presented below find two actors who cast together the most and list titles of only those movies they were casting together. Order the result set alphabetically by the movie title.
-- Table film_actor
-- Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- actor_id    | smallint                    | not null
-- film_id     | smallint                    | not null
-- ...
-- Table actor
-- Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- actor_id    | integer                     | not null
-- first_name  | character varying(45)       | not null
-- last_name   | character varying(45)       | not null
-- ...
-- Table film
-- Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- film_id     | integer                     | not null
-- title       | character varying(255)      | not null
-- ...
-- The desired output:
-- first_actor | second_actor | title
-- ------------+--------------+--------------------
-- John Doe    | Jane Doe     | The Best Movie Ever
-- ...
-- first_actor - Full name (First name + Last name separated by a space)
-- second_actor - Full name (First name + Last name separated by a space)
-- title - Movie title
-- Note: actor_id of the first_actor should be lower then actor_id of the second_actor

with film_actor_unique as
(select actor_id,film_id
from film_actor
group by actor_id,film_id
)

,detect_pair_freq as 
(select 
 fa.actor_id as first_actor
,sa.actor_id as second_actor
,fa.film_id
,row_number() over( partition by fa.actor_id,sa.actor_id ) as freq
from film_actor_unique fa
inner join film_actor_unique sa
  on  fa.film_id  = sa.film_id
  and fa.actor_id!= sa.actor_id
  and fa.actor_id< sa.actor_id
order by 1,2)


,most_frequent_pair as 
(
select 
 first_actor
,second_actor
,film_id
,freq
from detect_pair_freq  t
where freq in (select max(freq) from detect_pair_freq) 
)

,out as 
(select 
distinct
 actor_first.first_name  || ' ' || actor_first.last_name as first_actor 
,actor_second.first_name || ' ' || actor_second.last_name as second_actor 
,f.title
from detect_pair_freq mfp
inner join actor actor_first on actor_first.actor_id=mfp.first_actor
inner join actor actor_second on actor_second.actor_id=mfp.second_actor
inner join film f on mfp.film_id = f.film_id
where (first_actor,second_actor) in (select first_actor,second_actor from most_frequent_pair)
order by f.title asc
)

select *
from out