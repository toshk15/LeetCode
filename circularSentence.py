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

s = "the ilevator red deep put"
print(circularSentence(s))

    


