class Solution:
    def countAsterisks(self, s: str) -> int:
        ss=""
        su=0
        for i in s:
            if i=="|" or i=="*":
                ss+=i
        l=0
        a=0
        for ii in ss:
            if ii=="|":
                l+=1
            if ii=="*":
                a+=1
            if l==2:
                l=0
                a=0
            if l==0:
                su+=a
                a=0
        return su
    
"""
Example 1:

Input: s = "l|*e*et|c**o|*de|"
Output: 2
Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.

Example 2:

Input: s = "iamprogrammer"
Output: 0
Explanation: In this example, there are no asterisks in s. Therefore, we return 0.

Example 3:

Input: s = "yo|uar|e**|b|e***au|tifu|l"
Output: 5
Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are 5 asterisks considered. Therefore, we return 5.

"""