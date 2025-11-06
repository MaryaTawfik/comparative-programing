from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        product_count = defaultdict(int)
        
        # Count frequency of each product from all unique pairs
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        result = 0
        for count in product_count.values():
            if count > 1:
                result += count * (count - 1) * 4  # 8 * C(n, 2) = 4 * n * (n - 1)
        
        return result
