from pandasql import sqldf
sqldf('''
 with film as 
    ( select 300 as film_id,'codewars movie' as title)

    ,film_actor as
    ( select 1 as film_actor_id,122 as actor_id, 300 as film_id 
    union all 
    select 2 as film_actor_id,122 as actor_id,
    300 as film_id
    )

SELECT f.title
FROM film f
JOIN film_actor fa on fa.film_id = f.film_id
WHERE fa.actor_id IN (105,122)
GROUP BY f.film_id
HAVING COUNT(distinct actor_id) = 2
ORDER BY f.title ASC

''')