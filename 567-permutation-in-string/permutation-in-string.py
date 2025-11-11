from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        # Frequency of s1
        count1 = Counter(s1)
        # Frequency of first window in s2
        window = Counter(s2[:len1])
        
        if window == count1:
            return True
        
        # Slide the window
        for i in range(len1, len2):
            window[s2[i]] += 1          # add new char
            window[s2[i-len1]] -= 1     # remove old char
            if window[s2[i-len1]] == 0: # clean up zero counts
                del window[s2[i-len1]]
            
            if window == count1:
                return True
        
        return False
