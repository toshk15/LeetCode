class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk=[]
        d={c:i for i,c in enumerate(s)}
        for idx,ch in enumerate(s):
            if ch not in stk:
                while stk and idx<d[stk[-1]] and ch<stk[-1]:
                    stk.pop()
                stk.append(ch)
        return "".join(stk)
            
            
