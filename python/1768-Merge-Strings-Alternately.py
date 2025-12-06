def mergeAlternately(word1,word2):
    w1=len(word1)
    w2=len(word2)
    i,j=0,0
    s=""

    while i<w1 and j<w2:
        s+=word1[i]
        i+=1
        s+=word2[j]
        j+=1

    while i<w1:
        s+=word1[i]
        i+=1

    while j<w2:
        s+=word2[j]
        j+=1
    return s

word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1, word2))

"""
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

"""