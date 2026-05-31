class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        visited=set()
        left=0
        max_sum=0
        current_sum=0

        for right in range(len(nums)):
            if nums[right] in visited:
                while left<len(nums) and nums[right]  in visited:
                    current_sum-=nums[left]
                    visited.remove(nums[left])
                    left+=1
                    

            visited.add(nums[right])
            current_sum+=nums[right]
            # print(current_sum)
   
            max_sum=max(max_sum,current_sum)
        
        return max_sum
        