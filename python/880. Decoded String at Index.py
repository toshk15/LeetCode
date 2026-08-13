class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        ls=0
        for c in s:
            if c.isdigit():
                ls*=int(c)
            else:
                ls+=1
        for i in s[::-1]:
            k=k%ls
            if k==0 and i.isalpha():
                return i
            if i.isdigit():
                ls//=int(i)
            else:
                ls-=1
            
                
