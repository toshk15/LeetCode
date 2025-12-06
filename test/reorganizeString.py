def reorganizeString(s):
    s_len = len(s)
    count_char = {}

    for c in s:
        count_char[c] = 1 + count_char.get(c,0)
   
    max_freq = max(count_char.values())  

    if max_freq > (s_len + 1) // 2:
        return ""
    
    index = 0

    reorganize = [None] * s_len

    sortc = {k: v for k, v in sorted(count_char.items(), key=lambda item: item[1], reverse= True)}
    for c, f in sortc.items():
        while f:
            reorganize[index] = c
            f -= 1
            index += 2

            if index >= s_len:
                index = 1
    return "".join(reorganize)

s = "aabbbcc"
print(reorganizeString(s))