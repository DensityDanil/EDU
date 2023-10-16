select 
   rn
  ,sum(c1) over(order by rn asc)
  ,sum(c2) over(order by rn asc)
from 
(select c1,c2,row_number() over() rn
from
(
select CAST(36.77 AS FLOAT64) as c1,CAST(36.77 AS NUMERIC) as c2 union all
select CAST(36.77 AS FLOAT64) as c1,CAST(36.77 AS NUMERIC) as c2 union all
select CAST(36.88 AS FLOAT64) as c1,CAST(36.88 AS NUMERIC) as c2 union all
select CAST(36.88 AS FLOAT64) as c1,CAST(36.88 AS NUMERIC) as c2 union all
select CAST(36.94 AS FLOAT64) as c1,CAST(36.94 AS NUMERIC) as c2 union all
select CAST(36.77 AS FLOAT64) as c1,CAST(36.77 AS NUMERIC) as c2 union all
select CAST(36.92 AS FLOAT64) as c1,CAST(36.92 AS NUMERIC) as c2 union all
select CAST(36.92 AS FLOAT64) as c1,CAST(36.92 AS NUMERIC) as c2 union all
select CAST(36.92 AS FLOAT64) as c1,CAST(36.92 AS NUMERIC) as c2 union all

select CAST(36.77 AS FLOAT64) as c1,CAST(36.77 AS NUMERIC) as c2 union all
select CAST(36.77 AS FLOAT64) as c1,CAST(36.77 AS NUMERIC) as c2 union all
select CAST(36.88 AS FLOAT64) as c1,CAST(36.88 AS NUMERIC) as c2 union all
select CAST(36.88 AS FLOAT64) as c1,CAST(36.88 AS NUMERIC) as c2 union all
select CAST(36.94 AS FLOAT64) as c1,CAST(36.94 AS NUMERIC) as c2 union all
select CAST(36.77 AS FLOAT64) as c1,CAST(36.77 AS NUMERIC) as c2 union all
select CAST(36.92 AS FLOAT64) as c1,CAST(36.92 AS NUMERIC) as c2 union all
select CAST(36.92 AS FLOAT64) as c1,CAST(36.92 AS NUMERIC) as c2 union all
select CAST(36.92 AS FLOAT64) as c1,CAST(36.92 AS NUMERIC) as c2
) q ) q2
