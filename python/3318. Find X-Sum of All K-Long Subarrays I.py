class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n-k+1):
            c=Counter(nums[i:i+k])
            s=0
            if len(c)<x:
                s+=sum(nums[i:k+i])
                res.append(s)
            else:
                l=list(c.items())
                l.sort(key=lambda p: (p[1],p[0]),reverse=True)
                for i,j in l[:x]:
                    s+=(i*j)
                res.append(s)
        return res
            
                
