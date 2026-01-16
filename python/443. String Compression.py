def compress(chars):
    n=len(chars)
    k=i=0

    while i<n:
        chars[k]=chars[i]
        k+=1
        j=i+1
        while j<n and chars[i]==chars[j]:
            j+=1
        
        if j-i > 1:
            for c in str(j-i):
                chars[k]=c
                k+=1
        i=j
    return k

chars = ["a","a","b","b","c","c","c"]
#chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
d={"a":1}
print(len(d))
print(compress(chars))
