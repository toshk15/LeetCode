# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        length = mountainArr.length()
        r=length-1

        while l<r:
            m = l+(r-l)//2

            if mountainArr.get(m)<mountainArr.get(m+1):
                l=m+1
            else:
                r=m
          
        p=l
        ll=0
        r=p
        while ll<=r:
            m = ll+(r-ll)//2
            if mountainArr.get(m)<target:
                ll=m+1
            elif mountainArr.get(m)>target:
                r=m-1
            else:
                return m
        

        ll=l+1
        r=length-1
        while ll<=r:
            m = ll+(r-ll)//2
            if mountainArr.get(m)==target:
                return m                
            elif mountainArr.get(m)<target:
                r=m-1                
            else:
                ll=m+1        
                  
        return -1  
    
"""
Example 1:

Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

"""