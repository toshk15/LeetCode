class Solution:
    def numSub(self, s: str) -> int:
        cum=0
        c=0
        for n in s:
            if n == "1":
                c+=1
            elif n=="0":
                if c>0:
                    cum+=int(c*(c+1)/2)
                    c=0
                else:
                    continue
        if c>0:
            cum+=int(c*(c+1)/2)
        return cum%(10**9 + 7)
