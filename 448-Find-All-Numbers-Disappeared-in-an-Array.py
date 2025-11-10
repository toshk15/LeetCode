def findDisappearedNumbers(nums):
    s = set(nums)     
    res= set()
    for i in range(1,len(nums)+1):
        res.add(i)        
    res = res-s
    res=list(res)

    return res
    
nums = [4,3,2,7,8,2,3,1]