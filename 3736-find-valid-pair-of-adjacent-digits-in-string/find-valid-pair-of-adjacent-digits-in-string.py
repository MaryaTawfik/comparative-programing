from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        s_ = Counter(s)
        p1 = 0
        p2 = 1
        while p2 < len(s):
            if (s[p1] != s[p2] and 
                s_[s[p1]] == int(s[p1]) and 
                s_[s[p2]] == int(s[p2])):
                return f"{s[p1]}{s[p2]}"
            p1 += 1
            p2 += 1
        return ""
