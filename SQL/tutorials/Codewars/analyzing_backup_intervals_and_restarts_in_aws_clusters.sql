-- https://www.codewars.com/kata/652eac1a3a9be51b35dbfbbb/train/sql
-- Product IT Company uses AWS clusters for its operations and employs SSD-backed volumes within these clusters for regular data backups. Each cluster has a unique ID, and handles a series of backup tasks. Occasionally, backups on a cluster are restarted due to various reasons, leading to multiple 'Start' events before an 'End' event is logged for a backup task. Your role is to analyze the backup logs, ensuring each start event pairs with an end, and derive insights from these events.

-- We have backup_events table:

-- id (integer) - primary key.
-- event_datetime (timestamp) - The date and time of the backup event.
-- aws_cluster_id (integer) - A unique identifier for each AWS cluster.
-- backup_status (text) - Either 'Start' or 'End', indicating the backup event's status.
-- From the given database table, write an SQL query to:

-- Pair each backup start time with its corresponding end time.
-- Calculate the total duration of the backup.
-- Determine the number of restarts within each backup event.
-- Order the results by start_time in ascending order, and in the case of a tie - by aws_cluster_id also in asc order.
-- Assumptions:

-- There are no overlaps in the time frames for a given aws_cluster_id, meaning that a backup will end before another begins.
-- An 'End' event will always follow a 'Start' event for the same aws_cluster_id, but there may be multiple 'Start' events before an 'End' event if there are restarts.
-- Your resultant dataset should have:

-- start_time (text) - The timestamp of the backup start.
-- end_time (text) - The timestamp of the backup end.
-- aws_cluster_id (integer) - A unique identifier for the AWS cluster.
-- total_backup_duration - (interval) - Total time from start to end of the backup.
-- number_of_restarts - (integer) - Count of backup restarts within the respective backup duration.
-- For this sample data:

--  id | event_datetime        | aws_cluster_id | backup_status
-- ----+-----------------------+----------------+---------------
--  1  | 2023-07-09 03:00:00   | 33             | Start
--  2  | 2023-07-09 03:05:00   | 34             | Start
--  3  | 2023-07-09 03:10:00   | 35             | Start
--  4  | 2023-07-09 04:05:00   | 34             | End
--  5  | 2023-07-09 04:10:00   | 33             | Start
--  6  | 2023-07-09 05:05:00   | 33             | End
--  7  | 2023-07-09 05:10:00   | 34             | Start
--  8  | 2023-07-09 06:00:00   | 34             | End
--  9  | 2023-07-10 04:00:00   | 35             | Start
-- 10  | 2023-07-10 05:00:00   | 35             | Start 
-- 11  | 2023-07-11 05:00:00   | 35             | End
-- The expected output is the following:

--  start_time        | end_time          | aws_cluster_id | total_backup_duration | number_of_restarts
-- -------------------+-------------------+---------+-----------------------+-------------------
--  2023-07-09 03:00  | 2023-07-09 05:05  | 33             | 02:05:00              | 1
--  2023-07-09 03:05  | 2023-07-09 04:05  | 34             | 01:00:00              | 0
--  2023-07-09 03:10  | 2023-07-11 05:00  | 35             | 2 days 01:50:00       | 2
--  2023-07-09 05:10  | 2023-07-09 06:00  | 34             | 00:50:00              | 0
-- GLHF!

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
  ,sum(case when prev_status='End' then 1 else 0 end) over(partition by aws_cluster_id order by event_datetime) cluster_prev_status_end
from data)

,res as
(select 
   min(event_datetime)::text start_time        
  ,max(event_datetime)::text end_time         
  ,aws_cluster_id
  ,cluster_prev_status_end
  ,max(event_datetime) - min(event_datetime) as total_backup_duration 
  ,sum(case when backup_status='Start' then 1 end)-sum(case when backup_status='End' then 1 end) number_of_restarts
from sample
group by aws_cluster_id,cluster_prev_status_end
)


select start_time,end_time,aws_cluster_id,total_backup_duration,number_of_restarts
from res
order by start_time ,aws_cluster_id 

-- additional
-- method to define values of start without end

-- data = '''3	start
-- 3	start
-- 3	end
-- 3	start
-- 3	end'''.split('\n')

-- table_data = [(int(k.split('\table_data')[0]), k.split('\table_data')[1]) for k in data]

-- row_number=0
-- common_interval=0
-- struct = []
-- for table_tuple in table_data:
    
--     if table_tuple[1]!='end':
--         row = *table_tuple,row_number,common_interval
--         struct.append(row)
--         common_interval+=1
--     else:
--         row = *table_tuple,row_number,common_interval
--         struct.append(row)
--         row_number+=1
--         common_interval=0
        
-- print(*struct,sep='\n')