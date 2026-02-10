from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        ans=[]
        for key , value in freq.items():
            if value > len(nums)/3:
                ans.append(key)
        return ans
        