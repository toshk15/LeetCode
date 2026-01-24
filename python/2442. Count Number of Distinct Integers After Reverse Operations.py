class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res=[]
        res.extend(nums)
        counter=0
        for n in nums:
            re=int(str(n)[::-1])
            res.append(re)
        print(res)
        c=set(res)
        print(c)
        
        return len(c)
            
            
