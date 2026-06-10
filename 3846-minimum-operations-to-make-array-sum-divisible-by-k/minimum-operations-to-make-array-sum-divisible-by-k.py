class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        zsum=sum(nums)
        return zsum%k
        