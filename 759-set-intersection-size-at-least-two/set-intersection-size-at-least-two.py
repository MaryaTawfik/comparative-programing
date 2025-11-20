from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending, then start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        
        for start, end in intervals:
            count = 0
            # Count how many chosen numbers are already in [start, end]
            for num in res:
                if start <= num <= end:
                    count += 1
            
            # If fewer than 2, add new numbers from the end backward
            while count < 2:
                new_num = end - (1 - count)  # pick end, then end-1
                res.append(new_num)
                count += 1
        
        return len(res)
