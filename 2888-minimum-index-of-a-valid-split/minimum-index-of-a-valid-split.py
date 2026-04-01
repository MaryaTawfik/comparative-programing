from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #dominant = highest freq > len(nums//2)
        count=Counter(nums)
        dominant, total_count = count.most_common(1)[0]
        left_count=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]==dominant:
                left_count+=1
            if left_count *2 > (i+1):
                right_count = total_count - left_count
                if right_count *2 > (n-i-1):
                    return i
        return -1
                