from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=math.prod(nums)
        zero =nums.count(0)
        if zero > 1:
            return [0 for _ in range(len(nums))]
        if zero == 1:
            res=1
            for i in nums:
                if i != 0:
                    res *=i
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = res
                else:
                    nums[i] = 0
            return nums

        for i in range(len(nums)):
            nums[i] = int(m/nums[i])
        return nums
        


        
        
        
        
        





















        
        # n = len(nums)
        # answer = [1] * n

        # # Step 1: Prefix products
        # prefix = 1
        # for i in range(n):
        #     answer[i] = prefix
        #     prefix *= nums[i]

        # # Step 2: Suffix products
        # suffix = 1
        # for i in range(n-1, -1, -1):
        #     answer[i] *= suffix
        #     suffix *= nums[i]

        # return answer
