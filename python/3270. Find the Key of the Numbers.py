class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res=""
        n1 = "0"*(4-len(str(num1)))
        s1 = n1 + str(num1)
        n2 = "0"*(4-len(str(num2)))
        s2 = n2 + str(num2)
        n3 = "0"*(4-len(str(num3)))
        s3 = n3 + str(num3)
        for i in range(4):
            res+=min(s1[i],s2[i],s3[i])
        return int(res)
        
