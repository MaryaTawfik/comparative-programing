from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
                # min-queue 
        min_queue = deque()
        # max_queue
        max_queue = deque() 

        left = 0
        result = 0

        for right in range(len(nums)):
            # min_queue
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            min_queue.append(nums[right])
            
            # max_queue
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
            max_queue.append(nums[right])
            
            # operation
            while (max_queue[0] - min_queue[0]) > limit:
                first_num = nums[left]
                if first_num == max_queue[0]:
                    max_queue.popleft()
                if first_num == min_queue[0]:
                    min_queue.popleft()
                
                left += 1
            result = max(result, right - left + 1)
            
        return result 
            
            
            

                    
                # ans=0
                # for num in nums:
                #     if not queue:
                #         queue.append(num)
                #     else:
                #         queue.append(num)
                #         if max(queue) - min(queue)>limit:
                #             queue.pop(0)
                #     ans=max(ans,len(queue))
                # return ans

                        
                            
                
                