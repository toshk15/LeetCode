class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        c=Counter(ranks)
        cmax=max(c.values())
        if cmax>=3:
            return "Three of a Kind"
        elif cmax==2:
            return "Pair"
        else:
            return "High Card"
