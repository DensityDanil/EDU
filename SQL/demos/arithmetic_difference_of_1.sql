-- bq standard
with tmp as (

select 1 as rn union all
select 2 as rn union all
select 3 as rn union all
select 5 as rn 
)

select a.*
from tmp a left join tmp b on (b.rn-a.rn)=1
where a.rn IS NOT NULL AND b.rn IS NOT NULL
union distinct 
select b.*
from tmp a left join tmp b on (b.rn-a.rn)=1
where a.rn IS NOT NULL AND b.rn IS NOT NULL

-- output
-- 2
-- 3
-- 1