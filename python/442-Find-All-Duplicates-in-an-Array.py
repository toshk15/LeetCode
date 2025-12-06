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


"""
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []

"""