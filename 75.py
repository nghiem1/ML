def sort_color(nums):
    pivot=1
    smaller=0
    for i in range(0,len(nums)):
        if nums[i]<pivot:
            nums[smaller],nums[i]=nums[i],nums[smaller]
            smaller+=1
    larger=len(nums)-1
    for i in reversed(range(0,len(nums))):
        if nums[i]>pivot:
            nums[larger],nums[i]=nums[i],nums[larger]
            larger-=1
        elif nums[i]<pivot:
            break
    return nums

print(sort_color([2,0,2,1,1,0]))