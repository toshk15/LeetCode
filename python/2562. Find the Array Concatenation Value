class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        st=0
        r=len(nums)-1
        while l<=r:
            s=""
            if l==r:
                st+=nums[l]
            else:
                s=str(nums[l])+str(nums[r])
                st+=int(s)
            l+=1
            r-=1
        return st
            
            
        
