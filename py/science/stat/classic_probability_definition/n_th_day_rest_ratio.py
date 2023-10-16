
def prob(total_days
        ,total_works
        ,n_th_day
        ,n_th_day_works):

    total_in_days = n_th_day*n_th_day_works
    rest_days_works = (total_works - total_in_days)/(total_days - n_th_day)

    res = rest_days_works/total_works
    return res


r = prob(3,50,1,18)
r = prob(4,50,2,12)
r = prob(3,50,1,16)

