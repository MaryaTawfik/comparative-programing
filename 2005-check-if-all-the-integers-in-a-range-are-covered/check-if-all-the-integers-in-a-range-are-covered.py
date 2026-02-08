class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            num_covered=False
            for j in ranges:
                start=j[0]
                end=j[1]
                if start <= i <= end:
                    num_covered=True
                    break
            if not num_covered:
                return False
        return True
      
        