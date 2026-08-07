class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split()
        vowels=set("aeiouAEIOU")
        for i in range(len(s)):
            if s[i][0] in vowels:
                s[i]=s[i]+"ma"
            else:
                s[i]=s[i][1:]+s[i][0]+"ma"
            s[i]+="a"*(i+1)
        return " ".join(s)
