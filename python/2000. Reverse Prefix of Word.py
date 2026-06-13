class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=word.find(ch)
        s=word[:idx+1][::-1]+word[idx+1:]
        return s
