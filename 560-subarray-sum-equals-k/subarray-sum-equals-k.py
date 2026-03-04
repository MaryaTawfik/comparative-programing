from collections import defaultdict
# from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        my_dict = {0:1}
        current_sum=0
        for i in nums:
            current_sum += i
            if current_sum - k in my_dict:
                count+=my_dict[current_sum - k]
            my_dict[current_sum]=my_dict.get(current_sum,0) +1
        return count


        # ps=[0]+nums
        # print(ps)
        # for i in range(1,len(ps)):
            
        #     ps[i]+=ps[i-1]
        #     my_dict
        # for i in range(len(ps)):
        #     if ps[i] == k:
        #         return i



        # sum=[0]*(len(nums)+1)
        # count=0
        # freq=defaultdict(int)
        # freq[0]=1
        # for i in range (len(nums)):
        #     sum[i+1]=sum[i]+nums[i]
        #     count+=freq[sum[i+1]-k]
        #     freq[sum[i+1]]+=1
        # return count
        # sum=[0]*len(nums)
    
    