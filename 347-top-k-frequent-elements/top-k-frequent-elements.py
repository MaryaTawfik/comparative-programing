from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=Counter(nums)
        bucket_=bucket.most_common(k)
        return [num for num,freq in bucket_]














   

        