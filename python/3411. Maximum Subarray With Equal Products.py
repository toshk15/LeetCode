class Solution:
    def maxLength(self, nums: List[int]) -> int:
        #def gcd(a,b):
        #    while b:
        #        a,b=a,a%b
        #    return a
        #def lcm(a,b):
        #    if a==0 or b==0:
        #        return 0
        #    return abs(a*b)//gcd(a,b)
        n=len(nums)
        res=0
        for i in range(n):
            pro=1
            gcd_=0
            lcm_=1
            for j in range(i,n):
                pro=pro*nums[j]
                gcd_=math.gcd(gcd_,nums[j])
                lcm_=math.lcm(lcm_,nums[j])
                if pro==gcd_*lcm_:
                    res=max(res,j-i+1)
        return res
