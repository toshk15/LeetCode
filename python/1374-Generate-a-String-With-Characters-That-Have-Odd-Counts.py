class Solution:
    def generateTheString(self, n: int) -> str:
        s=""
        if n%2==0:
            for i in range(n-1):
                s+="a"
            s+=chr(ord("a")+1)
        else:
            for i in range(n):
                s+=chr(ord("a"))     
        return s
    
"""
Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

Example 3:

Input: n = 7
Output: "holasss"
"""