def findDuplicates(self, nums):
    s = set()
    res=[]
    for i in nums:
        if i not in s:
            s.add(i)
        else:
            if i not in res:
                res.append(i)
    return res
nums = [4,3,2,7,8,2,3,1]
