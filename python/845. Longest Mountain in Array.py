class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        res=0
        idx=0
        idy=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                idx=i
                idy=i
                while idx>0 and arr[idx]>arr[idx-1]:
                    idx-=1
            
                while idy+1 <len(arr) and arr[idy+1]<arr[idy]:
                    idy+=1
                res=max(res,idy-idx+1)
        return res
            
            
