-- https://www.codewars.com/kata/652eac1a3a9be51b35dbfbbb/train/sql

with data as (
select 
   aws_cluster_id
  ,event_datetime
  ,backup_status
  ,lag(backup_status) over(partition by aws_cluster_id order by event_datetime asc) prev_status
from backup_events

)

,sample as 
(select 
   aws_cluster_id
  ,event_datetime
  ,backup_status
  ,sum(case when prev_status='End' then 1 else 0 end) over(partition by aws_cluster_id order by event_datetime) c
from data)

,res as
(select 
   min(event_datetime)::text start_time        
  ,max(event_datetime)::text end_time         
  ,aws_cluster_id
  ,c
  ,max(event_datetime) - min(event_datetime) as total_backup_duration 
  ,sum(case when backup_status='Start' then 1 end)-sum(case when backup_status='End' then 1 end) number_of_restarts
from sample
group by aws_cluster_id,c
)


select start_time,end_time,aws_cluster_id,total_backup_duration,number_of_restarts
from res
order by start_time ,aws_cluster_id 

-- additional
-- data = '''3	start
-- 3	start
-- 3	end
-- 3	start
-- 3	end'''.split('\n')

-- t = [(int(k.split('\t')[0]), k.split('\t')[1]) for k in data]

-- c=0
-- s=0
-- struct = []
-- for i in t:
    
--     if i[1]!='end':
--         row = *i,c,s
--         struct.append(row)
--         s+=1
--     else:
--         row = *i,c,s
--         struct.append(row)
--         c+=1
--         s=0
        
-- print(*struct,sep='\n')