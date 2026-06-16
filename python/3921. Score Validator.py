class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        counter=0
        score=0
        res=[]
        for n in events:
            if n.isdigit() and counter!=10:
                score+=int(n)
            elif n=="W":
                if counter<10:
                    counter+=1
            else:
                if counter!=10:
                    score+=1
        res.append(score)
        res.append(counter)
        return res
