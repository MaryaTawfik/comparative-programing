from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_=deque()
        left=0
        right=0
        ans=[]
        while right<len(nums):
            while max_ and nums[max_[-1]]<nums[right]:
                max_.pop()
            max_.append(right)
            if left > max_[0]:
                max_.popleft()
            if (right+1)>=k:
                ans.append(nums[max_[0]])
                left+=1
            right+=1
        return ans
            


            