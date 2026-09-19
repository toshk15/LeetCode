class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        
        b=""
        nb=""
        while n:
            b=str(n%2)+b
            n//=2
        for i in b:
            if i=="0":
                nb+="1"
            else:
                nb+="0"
        print(nb)
        return int(nb,2)
