class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        sufix,prefix=p.split("*")
        su=len(sufix)
        pre=len(prefix)
        for i in range(len(s)):
            if s[i:].startswith(sufix) and prefix in s[i+su:]:
                return True
        return False
