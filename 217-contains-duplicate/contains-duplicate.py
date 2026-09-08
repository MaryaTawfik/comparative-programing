from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter=defaultdict(int)
        for i in nums:
            if counter[i] >0:
                return True
            counter[i] += 1
        else:
            return False
       
        
            
         
        
        