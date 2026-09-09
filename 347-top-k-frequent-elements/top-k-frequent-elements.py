from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq=Counter(nums)
        most_common=freq.most_common(k)
        return [i[0] for i in most_common]
        
        

       