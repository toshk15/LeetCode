class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c=0
        s=str(num)
        for n in range(len(s)-k+1):
            number=int(s[n:n+k])
            if number==0:
                continue
            else:
                if num%number==0:
                    c+=1
        return c
            
