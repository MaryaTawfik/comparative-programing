from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        numscount=Counter(nums)
        nums_=set(nums)
        res=[0]*2
        for i in range(n):
            if numscount[i+1] >1:
                res[0]=i+1
            if i+1 not in nums_:
                res[1]=i+1
        return res