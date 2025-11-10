"""
def decode(s):
    stackchar=[]
    stacknums=[]
   
    l,r =0,len(s)
 
    x=""
    while l<r:
        ss=""
        sf=""
        sn=""
        while s[l]!="]":
            if s[l].isdigit():
                stacknums.append(s[l])
            else:
                stackchar.append(s[l])
            l+=1
        l+=1    
            
        while stackchar[-1]!="[":
            sf+=stackchar.pop()
            
        sf=sf[::-1]

        stackchar.pop()

        while stacknums:
            sn+=stacknums.pop()
        sn = sn[::-1]

        ss=int(sn)*sf
        x+=ss
    return x
"""

def decodeString(s):
    stack=[]

    for c in s:
        if c != "]":
            stack.append(c)
        else:
            st=""
            while stack[-1] !="[":
                st = stack.pop()+st
            stack.pop()

            mul=""
            while stack and stack[-1].isdigit():
                mul = stack.pop() + mul
            
            stack.append(int(mul) * st)
    return "".join(stack)
#s = "3[a]2[bc]"

s = "2[abc]3[cd]ef"
print(decodeString(s))

"""
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""