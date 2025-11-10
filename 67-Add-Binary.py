class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa=int(a,2)
        bb=int(b,2)

        ss=aa+bb
        ss = bin(ss)
        print(ss)
        return str(ss[2:])
    
""" 
Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
""" 