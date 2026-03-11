from collections import Counter
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps= [0] + nums
        remenders=[]
        sum_=0

        for i in range(1,len(ps)):
            ps[i]+=ps[i-1]


        for i in ps:
            remender = i%k
            remenders.append(remender)
        
        remenders_counter = Counter(remenders)

        for key , value in remenders_counter.items():
            no_sub = (value *(value-1))//2
            sum_+=no_sub
        
        return sum_
            
        
        
        # no_sub = (m *(m-1))//2 
        # return no_sub

        

       
                



















        
        # sum=0
        # count=0
        # reminder_freq={0:1}
        # for i in range(len(nums)):
        #     sum=sum+nums[i]
        #     reminder=sum%k
        #     if reminder<0:
        #         reminder+=k
        #     if reminder in reminder_freq:
        #         count+=reminder_freq[reminder]
        #         reminder_freq[reminder]+=1
        #     reminder_freq[reminder]=1