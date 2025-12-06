def clearDigits(s):
    res = []
    delete_c = 0    

    for i in reversed(range(len(s))):
        if s[i].isdigit():
            delete_c += 1
        elif delete_c:
            delete_c -= 1
        else:
            res.append(s[i])
    return "".join(res[::-1])

"""
best sol:

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
"""

s = "abcd23"
#s = "23de"
#s = "23de9"
print(clearDigits(s))


"""
Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".
"""