def summaryRanges(nums):
    res=[]
    i = 0
    while i < len(nums):
        start = nums[i]

        while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
            i+=1
        if start != nums[i]:
            res.append(str(start)+ '->' + str(nums[i]))
        else:
            res.append(str(nums[i]))
        i+=1
    return res

nums=[0,1,2,4,5,7]
print(summaryRanges(nums))

"""


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

"""
      

            