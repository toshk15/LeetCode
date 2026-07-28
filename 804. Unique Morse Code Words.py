class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s=set()
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            ss=""
            for i in range(len(w)):
                ss+=code[ord(w[i])-ord("a")]
            s.add(ss)
        return len(s)
