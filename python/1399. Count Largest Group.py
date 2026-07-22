class Solution:
    def countLargestGroup(self, n: int) -> int:
        def add(num):
            s=0
            while num>0:
                s+=num%10
                num//=10
            #print(s)
            return s
        maxsum=0
        res=0
        d=defaultdict(int)
        for i in range(1,n+1):
            m=add(i)
            d[m]+=1
            maxsum=max(maxsum,d[m])
        for val in d.values():
            if maxsum == val:
                res+=1
        return res
        
            
    
            
    
