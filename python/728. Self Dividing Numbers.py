class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            f=False
            if '0' in str(i):
                continue
            for x in str(i):
                if i%int(x)==0:
                    f=True
                else:
                    f=False
                    break
            if f:
                res.append(i)
        return res
            
                    
                    
        
