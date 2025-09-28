def plusOne(digits):
    """
    s=""
    res=[]
    for i in digits:
        s+=str(i)
    s = int(s)
    s+=1
    s = str(s)

    for i in s:
        res.append(int(i))
        
    return res

    """

    n = len(digits)

    for i in range(n-1, -1, -1):
        digits[i]+=1
        digits[i]%=10
        if digits[i]!=0:
            return digits
    return [1] + digits

digits=[1,9,9]
print(plusOne(digits))
