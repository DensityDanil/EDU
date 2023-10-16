def dissasemble_hour_min(hour_min_value):
    hours,minutes = list(map(int,hour_min_value.split(':')))
    return hours,minutes


def timediff_cacl(gt_hour,lw_hour):

    
    delta_hours = gt_hour - lw_hour
    delta_minutes = (gt_minute - lw_minute)%60
    
    delta_minutes_rest = (gt_minute - lw_minute)//60
    delta_minutes_sum = delta_minutes + delta_minutes_rest

    

def hour_min_diff(greater,lower):
    gt_hour,gt_minute = dissasemble_hour_min(greater)
    lw_hour,lw_minute = dissasemble_hour_min(lower)

    delta_minutes  = (gt_minute - lw_minute)%60
    delta_minutes_rest = (gt_minute - lw_minute)//60
 
    delta_hours = (gt_hour - lw_hour)+delta_minutes_rest
    return delta_hours,delta_minutes
    
    

def next_cur( lst
             ,revese_neighbors_pos=False):
    first_idx,next_idx = 0,1 if revese_pos==False else 1,0
    
    return [(lst[i+first_idx],lst[i+next_idx]) for i in range(len(lst)-1)]
        
          
exp = ["23:00","04:22","18:05","06:24"]
exp = sorted(exp,key=lambda x:int(x.split(':')[0] ))[::-1]
#exp = next_cur(exp)


#res = [hour_min_diff(i[0],i[1]) for i in exp]

