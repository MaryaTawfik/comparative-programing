

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])  
        n = len(strs)    
        c = 0 

        for i in range(m):
            for j in range(1, n):
                if strs[j][i] < strs[j - 1][i]:
                    c += 1
                    break 

        return c

            
        