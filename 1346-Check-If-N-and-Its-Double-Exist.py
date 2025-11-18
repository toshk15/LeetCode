class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:       
        for n in range(len(arr)):
            for nn in range(n+1,len(arr)):               
                if 2*arr[n] == arr[nn] or arr[n]==arr[nn]*2:
                    return True  
        return False
    
"""
#using binary search

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        for i in range(n):
            target = 2 * arr[i]
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target and mid != i:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
"""
"""     
Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
""" 