class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        c=[]
        for i in range (0,len(nums),2):
            c.append(nums[i])
        total=sum(c)
        return total

        

