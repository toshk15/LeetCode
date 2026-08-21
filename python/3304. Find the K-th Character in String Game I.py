class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s)<=k:
            res=""
            for c in s:
                if c=="z":
                    res+="a"
                else:
                    res+=chr(ord(c)+1)
            s+=res
        return s[k-1]
