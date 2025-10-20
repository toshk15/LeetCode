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