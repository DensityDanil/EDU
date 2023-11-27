-- https://www.codewars.com/kata/649a8ed2c6ba0600314b258d/train/sql
-- Write an SQL query to find actors who have starred in a significant number of films (20 or more) 
-- and all of their films have enjoyed a certain level of commercial success, indicated by the films being rented 7 or more times 
-- we want to exclude any actors who have ever starred in a film that was rented less than 7 times. 
-- You need also to take into consideration films without rentals at all: 
-- actors who starred in such films should be excluded from the results as per the task's requirements.
-- Your SQL query should return a list of actors who satisfy the conditions specified above. 
-- For each actor, the output should include the following coluns:

with 
missing_films as (
select film_id
from film 
where film_id not in (select film_id from inventory) 
group by 1
)

,films_rented_more_or_eq_seven_times as (
select i.film_id,count(r.rental_id) rental_times
from inventory i
inner join rental r USING(inventory_id )
where film_id not in (select film_id from missing_films)
group by i.film_id 
-- and all of their films have enjoyed a certain level of commercial success, 
-- indicated by the films being rented 7 or more times
having count(distinct r.rental_id)>=7
order by 2 desc
) 

,exclude_actors as 
(select actor_id 
from film_actor
where film_id in (select film_id from missing_films)
group by 1
)

,only_needed as (
select actor_id 
from film_actor
-- here i filter rows
where film_id in (select film_id from films_rented_more_or_eq_seven_times)
group by 1
)

,another_except as 
(select actor_id
from film_actor 
where actor_id in (select actor_id from only_needed)
and film_id not in (select film_id from films_rented_more_or_eq_seven_times))

,res as 
(select actor_id,count(distinct film_id) film_count
from film_actor 

where 
  actor_id in (select actor_id from only_needed)
  and actor_id not in (select actor_id from exclude_actors)
  and actor_id not in (select actor_id from another_except)
group by actor_id 
having count(distinct film_id)>=20
)

select actor_id,first_name||' '||last_name full_name,film_count
from res
left join actor using(actor_id)
group by actor_id,first_name,last_name,film_count
order by film_count desc,actor_id asc
