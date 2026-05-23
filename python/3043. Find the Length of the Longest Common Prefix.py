class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res=0
        pre=set()
        for n in arr1:
            while n not in pre and n>0:
                pre.add(n)
                n=n//10
        for m in arr2:
            while m not in pre and m>0:
                m=m//10
            if m>0:
                res=max(res,len(str(m)))
        return res
                
                
            
