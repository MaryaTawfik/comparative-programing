from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_=Counter(nums)
        bas=[0,1,2]
        indx=0
        for i in bas:
            for j in range(nums_[i]):
                nums[indx]=i
                indx+=1
        
      
