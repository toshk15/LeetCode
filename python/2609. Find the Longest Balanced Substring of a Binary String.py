class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros=0
        ones=0
        res=0
        n=len(s)
        for i in range(n):
           if s[i]=="0":
              if i>0 and s[i-1]=="1":
                 zeros=0
                 ones=0
              zeros+=1
           else:
              ones+=1
              res=max(res,2*min(zeros,ones))
        return res
          
