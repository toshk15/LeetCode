class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        res=[]
        for n in s:
            if n.isdigit():
                res.append(int(n))
        print(res)
        for i in range(len(res)-1):
            if res[i+1]>res[i]:
                continue
            else:
                return False
        return True
                
