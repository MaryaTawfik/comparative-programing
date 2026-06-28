from collections import defaultdict
# from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict=defaultdict(int)
        prefix=[0]*(len(nums)+1)
        counter=0
        for i in range(1,len(prefix)):
            prefix[i]=prefix[i-1]+nums[i-1]
    
        for i in range(len(prefix)):
            if prefix[i]-k in my_dict:
                counter+=my_dict[prefix[i]-k]
            my_dict[prefix[i]]+=1
                
           
        
        return counter

            
            
     

        