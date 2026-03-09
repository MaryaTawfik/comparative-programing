from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]+nums
        right=nums+[1]
        ans=[]

        for i in range(1,len(nums)):
            left[i]*=left[i-1]

        for j in range(len(nums)-2,-1,-1):
            right[j]*=right[j+1]
        
        for i in range(1,len(right)):
            product = left[i-1] * right[i]
            ans.append(product)
        return ans

        
        





















        
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
