class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)

        vowels = max((c[i] for i in c if i in "aeiou"),default=0)
        consonants = max((c[i] for i in c if i not in "aeiou"), default=0)

        return vowels + consonants
    
    
"""
Example 1:

Input: s = "successes"

Output: 6

Explanation:

    The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
    The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
    The output is 2 + 4 = 6.

Example 2:

Input: s = "aeiaeia"

Output: 3

Explanation:

    The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
    There are no consonants in s. Hence, maximum consonant frequency = 0.
    The output is 3 + 0 = 3.

"""