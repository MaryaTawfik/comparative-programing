from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record last occurrence of each character
        last = {ch: i for i, ch in enumerate(s)}
        
        res = []
        start = end = 0
        
        # Step 2: Iterate through string
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:  # Partition boundary
                res.append(end - start + 1)
                start = i + 1
        
        return res
