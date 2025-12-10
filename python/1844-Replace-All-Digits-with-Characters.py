class Solution:
    def replaceDigits(self, s: str) -> str:
        ns=""
        def shift(char,num):
            newChar=ord(char)+num
            return chr(newChar)

        for n in range(len(s)):
            if n%2:
                x=shift(s[n-1],int(s[n]))
                ns+=x
            else:
                ns+=s[n]
        return ns
    
"""
Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'

Example 2:

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
"""