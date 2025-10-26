def lengthOfLastWord(s):
    s = s.split()
    s = s[-1]
    return len(s)

s="Hello World"
print(lengthOfLastWord(s))
