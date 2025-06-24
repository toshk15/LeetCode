"""
def valiPalindrom(s):
    newPal = ""
    
    for ca in s:
        if ca.isalnum():
            newPal += ca.lower()
    return newPal == newPal[::-1]
"""

def validPalindrom(s):
    l,r = 0, len(s) - 1

    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while r > l and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

def alphanum(c):
    return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))


s = "An#ita_lava_la_tina"
print(validPalindrom(s))