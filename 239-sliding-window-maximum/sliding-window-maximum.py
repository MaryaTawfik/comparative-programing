class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans=[]
        # [4,3,2,1]
        
        l,r=0,0
        que=collections.deque()
        while r<len(nums):
            while que and nums[r]>nums[que[-1]]:
                que.pop()
            que.append(r)
            if l > que[0]:
                que.popleft()
            if r+1 >= k:
                ans.append(nums[que[0]])
                l+=1
            r+=1
        return ans

        # # [3,2,-1,-3,5,3,6,7]
        # #    l  l    r
        # val[1,-3]
        # idx[2,3]
        # ans=[3,2]
        # left=0
        # right=k-1
        # # max_=nums[0]
        # # for i in range(k):
        # #     if max_ < nums[i]:
        # #         max_=nums[i]
        # # ans.append(max_)
        # while left<=right and right<len(nums):
        #     max_=float(-inf)
        #     for i in range(left,right+1):
        #         if max_ < nums[i]:
        #             max_=nums[i]
        #     ans.append(max_)
        #     left+=1
        #     right+=1
        # return ans

            
            

