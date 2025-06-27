class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m=list(set(nums))
        m.sort(reverse=True)
        n=len(m)
        if n>=3:
            return m[2]
        else:
            return m[0]
    
     
