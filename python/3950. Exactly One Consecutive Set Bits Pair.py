class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b=""
        res=0
        while n:
            b=str(n%2)+b
            n//=2
        print(b)
        for i in range(len(b)-1):
            if b[i]=="1" and b[i]==b[i+1]:
                res+=1
        return True if res==1 else False
            
