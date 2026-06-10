class Solution:
    def maxDistinct(self, s: str) -> int:
        
        counter_s = Counter(s)
        return len(counter_s)
        