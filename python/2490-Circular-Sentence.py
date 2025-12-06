"""
def circularSentence(s):
    words = s.split(" ")

    for i in range(len(words)):
        #print(words[-1][-1])
        if words[i][0] != words[i-1][-1]:
            return False
    return True

s = "the elevator red deep put"
print(circularSentence(s))
"""

def circularSentence(s):
    for i in range(len(s)):
        if s[i] == " " and s[i-1] != s[i+1]:
            return False
    return s[0] == s[-1]

sentence = "leetcode exercises sound delightful"
print(circularSentence(sentence))

    
"""
Example 1:

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

Example 2:

Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.

Example 3:

Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.
"""

