class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i in nums:
            m=float("-inf")
            for j in str(i):
                m = max(m, int(j))
            d[m].append(i)
        
        for key in d:
            d[key].sort(reverse=True)
        
        maxSum=-1
        for value in d.values():
            s=0
            i=0
            if len(value)==1:
                continue
            else:
                while i<2:
                    s+=value[i]
                    i+=1
            maxSum=max(maxSum,s)
        return maxSum

"""
Example 1:

Input: nums = [112,131,411]

Output: -1

Explanation:

Each numbers largest digit in order is [2,3,4].

Example 2:

Input: nums = [2536,1613,3366,162]

Output: 5902

Explanation:

All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

Example 3:

Input: nums = [51,71,17,24,42]

Output: 88

Explanation:

Each number's largest digit in order is [5,7,7,4,4].

So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

"""