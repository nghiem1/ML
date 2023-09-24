def longestcommonprefix(s):
    if len(s)==1 :
        return (s[0])
    if len(s)==0:
        return ('')
    
    pre=s[0]
    plen=len(pre)
    for i in s[1:] :
        while pre != i[0:]:
            pre=pre[0:(plen-1)]
            plen-=1
            if plen==0:
                return('')
    return pre


print(longestcommonprefix(['fra','frs']))