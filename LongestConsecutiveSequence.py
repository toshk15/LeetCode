def longestConsecutive(nums):
    l=0
    d={}
    for num in nums:
        d[num]=0
    for num in nums:
        curr_len=1
        next_num=num+1
        while next_num in d and d[next_num]==0:
            curr_len+=1
            d[next_num]=1
            next_num+=1
        prev_num = num-1
        while prev_num in d and d[prev_num]==0:
            curr_len+=1
            d[prev_num]=1
            prev_num-=1
        l = max(l,curr_len)
    return l

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))