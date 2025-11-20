class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start, path):
            # If combination is complete
            if len(path) == k:
                result.append(path[:])
                return
            
            # Try all possible next numbers
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # backtrack
        
        backtrack(1, [])
        return result
