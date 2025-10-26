def reverse_vowels(s):
    vowels = {"a":True, "e": True, "i": True, "o": True, "u":True, "A":True, "E":True, "I":True, "O": True, "U":True }

    if s == None or s == "" or len(s)==1:
        return s
    else:
        i = 0
        j = len(s)-1
        s = list(s)

        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue

            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return "".join(s)
    
s="hello"
    
print(reverse_vowels(s))


