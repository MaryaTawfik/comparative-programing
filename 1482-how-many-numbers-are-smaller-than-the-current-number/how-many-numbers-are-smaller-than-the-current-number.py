class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            num = sorted(nums)
            result = []

            for i in nums:
                count = 0
                
                for j in num:
                    if j < i:
                        count += 1
                    else:
                        break  
                
                result.append(count)
            
            return result
        
    
        
        