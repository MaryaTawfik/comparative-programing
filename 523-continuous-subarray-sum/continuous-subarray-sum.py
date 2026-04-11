from collections import Counter
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if len(nums) < 2:
            return False

        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False

        mapping = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            reminder = total % k

            if reminder in mapping:
                if i - mapping[reminder] >= 2:
                    return True
            else:
                mapping[reminder] = i

        return False