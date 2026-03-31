class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_=set(nums)
        max_=0

        for i in num_:
           
            if i-1 not in num_:
                curr=i
                cur_streak=1
                while curr+1 in num_:
                    curr+=1
                    cur_streak+=1
                max_=max(max_,cur_streak)
        return max_


       
    