class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            res=[]
            for n in x:
                m=0
                sr = str(n)
                for i in range(len(sr)):
                    m=max(m,int(sr[i]))
                m=str(m)*len(sr)
                res.append(int(m))
            return sum(res)
        return encrypt(nums)
        
                    
            
