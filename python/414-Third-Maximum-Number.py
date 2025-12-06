def thirdMax(nums):
    s = set(nums)
    s=list(s)
    s.sort()
    if len(s)==1:
        return s[0]
    if len(s)==2:
        if s[-1]>s[-2]:
            return s[-1]
        else:
            return s[-2]        
    else:
        return s[-3]
    
nums = [1,2]