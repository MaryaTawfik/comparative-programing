from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_=list(s)
        t_=list(t)
        s_.sort()
        t_.sort()
        return s_ == t_
       
        