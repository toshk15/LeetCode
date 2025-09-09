from collections import Counter
from collections import defaultdict

def subsetWords(words1, words2):
    count_2 = defaultdict(int)

    for w in words2:
        count_w = Counter(w)
        for c, cnt in count_w.items():
            count_2[c] = max(count_2[c], cnt)
        
    res = []
    for w in words1:
        count_w = Counter(w)
        flag = True
        for c, cnt in count_2.items():
            if count_w[c] < cnt:
                flag = False
                break
        if flag:
            res.append(w)
    return res



words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]

print(subsetWords(words1, words2))

