class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def diff(n):
            s=str(n)
            mi=10
            ma=-1
            for i in range(len(s)):
                mi=min(int(s[i]),mi)
                ma=max(int(s[i]),ma)
            return ma-mi
        d={x:diff(x) for x in nums}
        m=max(d.values())
        print(m)
        res=0
        for x in nums:
            if d[x]==m:
                res+=x
        return res
                
                
