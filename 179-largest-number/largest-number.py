class Solution:
    def largestNumber(self, nums):
        
        nums = [str(x) for x in nums]
        n = len(nums)

        
        for i in range(n):
            for j in range(i + 1, n):
                
                if nums[i] + nums[j] < nums[j] + nums[i]:
                   
                    nums[i], nums[j] = nums[j], nums[i]

        
        if nums[0] == "0":
            return "0"

       
        return "".join(nums)