class Solution:
    def digitCount(self, num: str) -> bool:
        c=[0]*10
        for i in range(len(num)):
            c[int(num[i])]+=1
        for i in range(len(num)):
            if int(num[i])!=c[i]:
                return False
        return True
