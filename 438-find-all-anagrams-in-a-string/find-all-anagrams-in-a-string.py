from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = Counter(p)
        window_count = Counter()

        for i in range(len(s)):
        # Add current character to the window
            window_count[s[i]] += 1

        # Remove character left of the window if window size exceeds p
            if i >= len(p):
                if window_count[s[i - len(p)]] == 1:
                    del window_count[s[i - len(p)]]
                else:
                    window_count[s[i - len(p)]] -= 1

        # Compare window with p_count
            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result
        