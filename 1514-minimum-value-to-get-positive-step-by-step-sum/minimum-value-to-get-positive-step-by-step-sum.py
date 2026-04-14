class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        def isvalid(start):
            current= start
            for i in nums:
                current+=i
                if current<1:
                    return False
            return True

        left,right=1,10001
        ans=right

        while left<=right:
            mid=(left+right)//2

            if isvalid(mid):
                answer=mid
                right=mid-1
            else:
                left=mid+1

        return answer

        