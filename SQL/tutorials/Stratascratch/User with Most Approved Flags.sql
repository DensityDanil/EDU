#https://platform.stratascratch.com/coding/2104-user-with-most-approved-flags?code_type=3
with distinct_videos_aporve_by_youtube_sample as 
(select 
       concat(ifnull(user_firstname,'Empty'),' ', ifnull(user_lastname,'Empty') ) as user_fullname
      ,count(distinct case when flag_id is not null or trim(flag_id)!='' then video_id end) as approve_count
      ,group_concat(distinct case when flag_id is not null or trim(flag_id)!='' then video_id end) as approve_lst
     -- ,sum(case when flag_id is not null or trim(flag_id)!='' then 1 else 0 end) as approve_count
     -- ,group_concat(flag_id)
    
from user_flags
where video_id is not null or trim(video_id)!=''
group by 1
order by 2 desc
)
-- ('5qap5aO4i9A','video_id with user-, flag-')
-- ('Lopez','name-')

select user_fullname
from distinct_videos_aporve_by_youtube_sample
where approve_count in (select max(approve_count) from distinct_videos_aporve_by_youtube_sample)
-- user count 
    -- help find max
-- video for one or many
-- flag is unique
-- default value if null for platform approve
