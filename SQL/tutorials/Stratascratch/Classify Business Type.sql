#https://platform.stratascratch.com/coding/9726-classify-business-type?code_type=3

select 
     business_name
    ,case 
    when lower(business_name) regexp 'caf[e|e]|coffee' then 'cafe'
    when lower(business_name) regexp 'school' then 'school'
    when lower(business_name) regexp 'restaurant' then 'restaurant'
    else 'other'
    end as class
from sf_restaurant_health_violations
group by business_name
order by 2 asc
;