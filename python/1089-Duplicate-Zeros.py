class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """  
        ss=""
        for i in arr:
            if i!=0:
                ss+=str(i)
            elif i==0:
                ss+="00"
        i=0
        while i<len(arr):
            arr[i]=int(ss[i])
            i+=1
            
"""
Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

"""
                