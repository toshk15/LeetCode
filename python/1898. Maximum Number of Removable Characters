class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def sub(s,sub,remo):
            i=0
            j=0
            while i<len(s) and j <len(sub):
                if i in remo or s[i]!=sub[j]:
                    i+=1
                    continue
                i+=1
                j+=1
            return j==len(sub)
        res=0
        l,r=0,len(removable)-1
        while l<=r:
            m=(l+r)//2
            remo=set(removable[:m+1])
            if sub(s,p,remo):
                res=max(res,m+1)
                l=m+1
            else:
                r=m-1
        return res
                



            
