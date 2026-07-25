class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left=right=0
        nums.sort()
        length=0
        while left<=right and right<len(nums):
            if nums[right]-nums[left]>1:
                left+=1
            elif nums[right]-nums[left]<1:
                right+=1
            elif nums[right]-nums[left] == 1:
                length=max(right-left+1 , length)
                right += 1
        return length

        