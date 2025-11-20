from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, total):
            # Base case: found a valid combination
            if total == target:
                result.append(list(current))
                return
            # If sum exceeds target, stop
            if total > target:
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # allow reuse of same candidate
                current.pop()  # backtrack

        backtrack(0, [], 0)
        return result
