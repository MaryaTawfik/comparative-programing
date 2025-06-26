from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for i ,j in c.items():
            if j >=2:
               return True
        return False

        
            
         
        
        