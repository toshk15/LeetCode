class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        sf=""
        for i in words:
            sf+=i
            if s==sf:
                return True
        return False
    
"""
Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
"""