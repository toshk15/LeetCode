class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:       
        arr.sort()
        res=[]
        m=float("inf")
        for n in range(len(arr)-1):
            diff = arr[n+1]-arr[n]
            if diff<m:
                m=diff
        for n in range(len(arr)-1):
            if arr[n+1]-arr[n] == m:
                res.append([arr[n],arr[n+1]])
        return res
        
"""
Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

"""