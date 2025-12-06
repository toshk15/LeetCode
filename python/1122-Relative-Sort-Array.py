class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res=[]
        res2=[]
        for i in arr2:
            while c[i]>0:
                res.append(i)
                c[i]-=1
            del c[i]
        for i in c:
            while c[i]>0:
                res2.append(i)
                c[i]-=1
        return res+sorted(res2)
    
"""
 
Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""