class Solution:
    def splitNum(self, num: int) -> int:
        res=[]
        s=str(num)
        for i in range(len(s)):
            res.append(int(s[i]))
        res.sort()
        num1=0
        num2=0
        for i in range(len(res)):
            if i%2:
                num2=num2*10+res[i]
            else:
                num1=num1*10+res[i]
        return num1+num2
                
