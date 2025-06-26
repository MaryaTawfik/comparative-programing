class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                  k.append(i)
                  k.append(j)
        return list(set(k)) 
        