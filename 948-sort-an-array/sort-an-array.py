from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def divide(left, right):
            if left == right:
                return [nums[left]]
            
            mid = (left + right) // 2
            left_part = divide(left, mid)
            right_part = divide(mid + 1, right)
            
            return merge(left_part, right_part)
        
        
        def merge(left, right):
            i, j = 0, 0
            result = []
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        
        return divide(0, len(nums) - 1)