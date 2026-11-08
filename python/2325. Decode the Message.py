class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        abc='abcdefghijklmnopqrstuvwxyz'
        m={" ":" "}
        i=0
        res=""
        for c in key:
            if c not in m:
                m[c]=abc[i]
                i+=1
        for c in message:
            res+=m[c]
        return res
            
