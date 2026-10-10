class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        res=-1
        n = len(strs)
        def sub(a,b):
            i=0
            j=0
            while i<len(a) and j<len(b):
                if a[i]==b[j]:
                    j+=1
                i+=1
            return j==len(b)
        for i in range(n):
            j=0
            while j<n:
                if i==j or not sub(strs[j],strs[i]):
                    j+=1
                else:
                    break
            if j==n:
                res=max(res,len(strs[i]))
        return res
            
            
