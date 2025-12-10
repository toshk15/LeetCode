class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=set("aeiou")
        c=0
        for idx in range(len(word)):
            v=set()
            for char in word[idx:]:
                if char not in vowels:
                    break
                v.add(char)
                if len(v)==5:
                    c+=1
        return c
            
"""
Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

"""