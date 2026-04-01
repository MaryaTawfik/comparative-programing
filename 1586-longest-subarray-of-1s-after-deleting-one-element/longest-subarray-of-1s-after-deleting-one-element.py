class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counter=0
        l,r=0,0
        length=0
        while r < len(nums) and l<=r:
            if nums[r]==0:
                counter+=1
            # length=max(length,r-l)
            while counter >1:
                if nums[l]==0:
                    counter-=1

                l+=1
                # counter-=1
            length=max(length,r-l)
            r+=1
        return length
            