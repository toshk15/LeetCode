class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ws="".join(sorted(words[0]))
        result=[words[0]]
        prev=ws
        for w in words[1:]:
            curr="".join(sorted(w))
            if curr != prev:
                result.append(w)
                prev=curr
        return result
