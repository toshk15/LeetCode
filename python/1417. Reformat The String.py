class Solution:
    def reformat(self, s: str) -> str:
        res=[0]*len(s)
        letters=[i for i in s if i.isalpha()]
        numbers=[i for i in s if i.isdigit()]
        if abs(len(letters)-len(numbers))>1:
            return ""
        if len(letters)<len(numbers):
            letters,numbers=numbers,letters
        i=0
        j=0
        while i < len(s):
            res[i]=letters[j]
            i+=2
            j+=1
        i=1
        j=0
        while i < len(s):
            res[i]=numbers[j]
            i+=2
            j+=1
        return "".join(res)
        
        
        
