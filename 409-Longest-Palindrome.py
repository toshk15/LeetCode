from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:    
        n=0      
        c = Counter(s)
        if len(c)==1:
            return len(s)
        for j in c.values():
            n += (j//2) *2            
                
        for v in c.values():
            if v%2==1:
                n+=1  
                break              
      
        return n
    
"""
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""