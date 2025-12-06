class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        counter={}
        for c in ".!?',;:":
            paragraph=paragraph.replace(c," ")

        paragraph = paragraph.split()
        s=set(banned)

        for w in paragraph:
            if w not in s:
                counter[w]=counter.get(w,0)+1  
        m=0
        wo=""
        for i,j in counter.items():
            if j>m:
                m=j
                wo=i

        return wo
    
"""

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

"""