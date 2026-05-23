class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary=""
        odd=0
        even=0
        while n>0:
            binary = str(n%2)+binary
            n=n//2
        binary=binary[::-1]
        for i in range(len(binary)):
            if i%2 and binary[i]=="1":
                odd+=1
            elif i%2==0 and binary[i]=="1":
                even+=1
        return [even,odd]
            
            
