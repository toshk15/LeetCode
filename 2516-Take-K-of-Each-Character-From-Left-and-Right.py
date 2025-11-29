class Solution:
    def takeCharacters(self, s: str, k: int) -> int:            
        l=0
        n=len(s)
        res=float("inf")
        c={"a":0,"b":0,"c":0}
        for letter in s:
            c[letter]+=1            

        values = min(c.values())
        if values < k:
            return -1

        for r in range(n):
            c[s[r]]-=1
            while min(c.values())<k:
                c[s[l]]+=1
                l+=1
            diff=n-(r-l+1)
            res=min(res,diff )            
        return res
    
"""

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.


"""