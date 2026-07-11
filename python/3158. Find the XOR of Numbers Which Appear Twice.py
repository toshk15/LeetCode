class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c=Counter(nums)
        res=[]
        print(c)
        for k,v in c.items():
            if v==2:
                res.append(k)

        if len(res)==0:
            return 0
        
        x=res[0]
        for i in range(1,len(res)):
            x^=res[i]
        return x
        

            
