def rearrangeArray(self, nums: List[int]) -> List[int]:
    pos=[]
    neg=[]

    for i in nums:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
   
    i,j,k = 0,0,0
    while i < len(pos) and j<len(neg):
        nums[k]=pos[i]
        k+=1
        nums[k]=neg[j]
        k+=1
        i+=1
        j+=1

    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num 
                neg += 2
        
        return ans
    """
    return nums
"""
Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

"""