class Solution:
    def sortVowels(self, s: str) -> str:
        resVowels=[]
        vowels={"a","e","i","o","u", "A", "E","I","O","U"}       
        for i in s:
            if i in vowels:
                resVowels.append(i)
        resVowels.sort()
        resString=list(s)
        idx=0
        for i, char in enumerate(resString):
            if char.lower() in "aeiou":
                resString[i] = resVowels[idx]
                idx += 1        
        return "".join(resString)
    
"""
Example 1:

Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.

Example 2:

Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".

"""