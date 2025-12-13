class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        maxfre=float("-inf")
        res=[]
        aux=0
        for i in nums:
            if i%2==0:
                res.append(i)
        c=Counter(res)
        sorted_c = sorted(c.items(), key=lambda item: item[0])
        sorted_c = dict(sorted_c)
        for i,j in sorted_c.items():
            if j>maxfre:
                maxfre=j
                aux=i
        return -1 if maxfre==float("-inf") else aux
    
"""
Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

"""