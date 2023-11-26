from duckdb import sql
from tests import tests

import sys
sys.path.append(r"W:\github\funcs\my_pandas\run_pds_sql")
from create_log_file import *


def run_cte(query,cte_alias):
    cte = f"""
    {query}

    select *
    from {cte_alias}
    """
    return sql(cte).df()


#NEED RESTART 
actor_appearance = 1
film_rentals = 7

query = f'''
with 
missing_films as (
select film_id,'where inventory_id not in (select inventory_id from rental)'
from inventory 
where inventory_id not in (select inventory_id from rental)
group by 1

union
  
select film_id ,'where film_id not in (select film_id from inventory) '
from film 
where film_id not in (select film_id from inventory) 
group by 1
)

,actor_test as 
(
select *
from 
(select 
       actor_id,film_id,row_number() over(partition by actor_id) rn
from 
      film_actor
group by 
      actor_id,film_id) q where rn>={actor_appearance}
)
 
 
,films_rented_more_then_seven_times as (
select i.film_id,count(r.rental_id) rental_times
from inventory i
inner join rental r USING(inventory_id )
where film_id in (select film_id from actor_test) 
    and film_id not in (select film_id from missing_films)
group by i.film_id 
having count(distinct r.rental_id)>={film_rentals}
order by 2 desc
) 

,not_rental_actors as (
select actor_id
from film_actor 
where film_id in (select film_id from missing_films)
group by actor_id
)

,res as (
select * 
from
(select 
       actor_id
from 
      film_actor
where film_id in (select film_id from films_rented_more_then_seven_times)
and actor_id not in (select actor_id from not_rental_actors)
group by 
      actor_id
 having count(distinct film_id)>={actor_appearance}
 ) q 
)

select *
from res
'''

# counter=0
# while True:
#   try:
#     film, film_actor, actor, rental, inventory = tests(test_idx=counter)
#     print(run_cte(query,'res'))
#   except Exception as e:
#     print(str(e))
#     break
#   counter+=1
# #run_cte(query,'not_rental_films')==run_cte(query,'films_only_in_inventory')