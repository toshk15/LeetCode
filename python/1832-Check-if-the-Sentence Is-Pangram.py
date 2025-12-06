def pan(s):
    lowercase_alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
    print(lowercase_alphabet)
    x = set(lowercase_alphabet)

    for i in s:
        if i in x:
            x.remove(i)
    if not x:
        return True
    else:
        return False

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(pan(sentence))