def singleNumber(nums):
    c = {}
    for i in nums:
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
       
    keys = [key for key, val in c.items() if val == 1]
        
    return keys[0]
        