def solution(s):
    out = None
    if len(s)%2==1:
        s = s+'_'
        out = [s[k:k+2] for k in range(0,len(s),2)]
    else:
        out = [s[k:k+2] for k in range(0,len(s),2)]
    return out