class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        current_sum=0
        prefix_sum=0
        my_dict={0:1}
        for i in nums:
            current_sum+=i
            needed=current_sum -goal
            if needed in my_dict:
                count+=my_dict[needed]
            if current_sum in my_dict:
                my_dict[current_sum]+=1
            else:
                my_dict[current_sum]=1
        return count

        