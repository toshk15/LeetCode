def reverseWords(s):
    res=[]    
    s = s.split()
    for i in s:        
        res.append(i[::-1])
    return " ".join(res)