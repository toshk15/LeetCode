def detectCapitalUse(word):
    """
    if word.isupper() or word.islower():
        return True

    if word[0].isupper() and word[1:].islower():
        return True
    else:
        return False
    """
    l = len(word)
    cap=0
    nocap=0
    s=0
    for i in range(l):
        if word[i].isupper():
            cap+=1
        if word[i].islower():
            nocap+=1
        if i<l-1 and word[0].isupper():
            if word[i+1].islower():
                s+=1
        if s==l-1:
            return True

        if cap==l:
            return True
           
        if nocap==l:
            return True
    return False

word = "Leetcode"
print(detectCapitalUse(word))
    
"""
Example 1:

Input: word = "USA"
Output: true

Example 2:

Input: word = "FlaG"
Output: false

"""
