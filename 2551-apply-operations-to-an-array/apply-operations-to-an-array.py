class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]*=2
                nums[i]=0
        zeros=[]
        for j in nums:
            if j == 0:
                
                zeros.append(j)
        ans=[]
        for i in nums:
            if i != 0:
                ans.append(i)
        ans.extend(zeros)
        return ans