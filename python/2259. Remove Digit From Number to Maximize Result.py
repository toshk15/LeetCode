class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res=0
        for i in range(len(number)):
            if number[i]==digit:
                n = number[:i]+number[i+1:]
                ns=int(n)
                if ns>res:
                    res=ns
        return str(res)
