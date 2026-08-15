import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        m= [list(i) for i in itertools.permutations(nums)]
        return m

