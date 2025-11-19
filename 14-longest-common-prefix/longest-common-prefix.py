from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the array so the most different strings are at the ends
        strs.sort()
        
        # Compare only the first and last strings
        first, last = strs[0], strs[-1]
        prefix = []
        
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix.append(first[i])
            else:
                break
        
        return "".join(prefix)
