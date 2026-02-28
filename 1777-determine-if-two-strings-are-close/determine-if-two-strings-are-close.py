from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if not set(word1).issubset(set(word2)):
            return False
        w1 = Counter(word1)
        w2 = Counter(word2)
        w1_=sorted(w1.values())
        w2_=sorted(w2.values())
        for i in range(len(w1)):
            if w1_ [i] != w2_[i]:
                return False  
        return True


        