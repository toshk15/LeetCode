def maximumGain(s,x,y):
    total=0
    high_priority="ab"
    low_priority="ba"

    if x<y:
        x,y =y,x
        high_priority, low_priority = low_priority, high_priority
    stack=[]
    for char in s:
        if char==high_priority[1] and stack and stack[-1] == high_priority[0]:
            stack.pop()
            total+=x
        else:
            stack.append(char)
    stacknew=[]
    for char in stack:
        if char==low_priority[1] and stacknew and stacknew[-1]==low_priority[0]:
            stacknew.pop()
            total+=y
        else:
            stacknew.append(char)
    return total

s = "cdbcbbaaabab"
x = 4
y = 5

#s = "aabbaaxybbaabb"
#x = 5
#y = 4
print(maximumGain(s,x,y))
