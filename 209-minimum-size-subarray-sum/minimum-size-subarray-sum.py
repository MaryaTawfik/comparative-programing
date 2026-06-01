class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # prefix_sum=[0]*(len(nums))
        
        # for i in range(1,len(nums)):
        #     prefix_sum[i]=prefix_sum[i-1]+nums[i]
        # print(prefix_sum)

        left=0
        min_len=float('inf')
        current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            if current_sum < target:
                
                continue
            min_len=min(min_len,right-left+1)
            while current_sum >= target:
                # left+=1
                min_len=min(min_len,right-left+1)
                current_sum-=nums[left]
                left+=1
                
                    # min_len=min(min_len,right-left+1)
                
            
            # if current_sum >= target:
            #     min_len=min(min_len,right-left+1)

        return min_len if min_len != float('inf') else 0

        