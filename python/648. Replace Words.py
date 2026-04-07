class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence=sentence.split()
        for i in range(len(sentence)):
            for w in dictionary:
                if w in sentence[i][:len(w)]:
                    sentence[i]=w
        return " ".join(sentence)
