class Solution:
    def greatestLetter(self, s: str) -> str:
        ss=set(s)
        res=""
        for c in s:
            if c.isupper():
                if c in ss and c.lower() in ss:
                    if c>res:
                        res=c
        return res
