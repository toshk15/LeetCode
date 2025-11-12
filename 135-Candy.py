class Solution:
    def candy(self, ratings: List[int]) -> int:
        res=[1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        for i in range(len(ratings)-1,-1,-1):
            if i>0 and ratings[i]<ratings[i-1]:
                if res[i]<res[i-1]:
                    continue
                else:
                    res[i-1]=res[i]+1
        return sum(res)

"""
Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""