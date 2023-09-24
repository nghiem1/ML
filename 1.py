def tow_sum(nums,target):
    dt={}
    for idx,num in enumerate(nums):
        if (target-num) in dt:
            return (dt[target-num],idx) 
        else:
            dt[num]=idx
    print(dt)
print(tow_sum([2,7,3,5],10))