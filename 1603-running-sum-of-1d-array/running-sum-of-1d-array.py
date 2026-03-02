class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_=0
        ans=[]
        for i in nums:
            sum_+=i
            ans.append(sum_)
        return ans
            

    