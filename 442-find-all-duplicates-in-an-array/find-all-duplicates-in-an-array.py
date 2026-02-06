from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1=Counter(nums)
        res=[]
        for key,val in dict1.items():
            if val==2:
                res.append(key)
        return res

        