class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        s=n1+n2+n3
        m=min(n1,n2,n3)
        if s1[0]!=s2[0] or s1[0]!=s3[0] or s2[0]!=s3[0]:
            return -1
        for i in range(m):
            if s1[i]==s2[i] and s2[i]==s3[i] and s1[i]==s3[i]:
                s-=3
            else:
                break
        return s
            
            
