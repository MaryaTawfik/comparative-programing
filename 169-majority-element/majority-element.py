from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict = Counter(nums)
        
        for i,j in freq_dict.items():
            if j>len(nums)//2:
                return i
                
        
        

        